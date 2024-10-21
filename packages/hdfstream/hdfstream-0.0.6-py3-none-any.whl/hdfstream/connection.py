#!/bin/env python

import os
import getpass
import functools
import codecs

import requests
import msgpack
import msgpack_numpy as mn
import numpy as np

from hdfstream.exceptions import HDFStreamRequestError


# Allow disabling SSL certificate verification and associated warnings (useful for testing)
verify_cert = True
def disable_verify_cert():
    global verify_cert
    import urllib3
    urllib3.disable_warnings()
    verify_cert = False


def decode_hook(data):
    """
    Converts dicts decoded from the msgpack stream into numpy ndarrays. Called
    by msgpack.unpack().

    Dicts with nd=True contain a binary buffer which should be wrapped with a
    numpy array with type and shape given by the metadata in the dict. We call
    msgpack-numpy's decode() function to do this.
    
    Dicts with vlen=True contain flattened lists of variable size
    elements and are translated into numpy object arrays.
    """
    # If this is a serialized ndarray, use msgpack-numpy to decode it
    data = mn.decode(data)

    # Then check for any vlen data: in that case we have a flattened list
    # which needs to be converted into an object array of the right shape.
    if isinstance(data, dict):
        if b"vlen" in data:
            # Get the shape of the array
            shape = [int(i) for i in data[b"shape"]]
            if len(shape) == 0:
                # For scalars, just return the value
                data = data[b"data"][0]
            else:
                # Otherwise we make an object array
                arr = np.empty(len(data[b"data"]), object)
                arr[:] = data[b"data"]
                data = arr.reshape(shape) 
    return data


def raise_for_status(response):
    """
    Check the http response status and raise an exception if necessary

    This also extracts the error message from the response body, if
    there is one.
    """
    if not response.ok:
        if response.status_code == 401:
            # Catch case of wrong password
            raise HDFStreamRequestError("Not authorized. Incorrect username or password?")
        try:
            # Extract msgpack encoded error string from response.
            # decode_content=True is needed if the response is compressed.
            response.raw.read = functools.partial(response.raw.read, decode_content=True)
            data = msgpack.unpack(response.raw)
            message = data["error"]
        except Exception:
            # If we don't have a message from the server, let the requests
            # module generate an exception
            response.raise_for_status()
        else:
            # Raise an exception using the error message
            raise HDFStreamRequestError(message)


class Connection:
    """
    Class to store http session information and make requests
    """
    _cache = {}
    
    def __init__(self, server, user=None, password=None):

        # Remove any trailing slashes from the server name
        self.server = server.rstrip("/")
    
        # Set up a session with the username and password
        if user is None:
            user = getpass.getpass("User: ")
        self.user = user
        if password is None:
            password = getpass.getpass("Password: ")
        self.session = requests.Session()
        self.session.auth = (user, password)

        # Test credentials by fetching a directory listing
        response = self.session.get(self.server+"/msgpack/FLAMINGO", verify=verify_cert)
        raise_for_status(response)

    @staticmethod
    def new(server, user, password=None):

        # Remove any trailing slashes from the server name
        server = server.rstrip("/")
        
        # Connection ID includes process ID to avoid issues when session
        # objects are reused between processes (e.g. with multiprocessing).
        connection_id = (server, user, os.getpid())

        # Open a new connection if necessary
        if connection_id not in Connection._cache:
            Connection._cache[connection_id] = Connection(server, user, password)
        return Connection._cache[connection_id]

    def get_and_unpack(self, url, params=None):
        """
        Make a request and unpack the response
        """
        with self.session.get(url, params=params, stream=True, verify=verify_cert) as response:        
            raise_for_status(response)
            response.raw.read = functools.partial(response.raw.read, decode_content=True)
            data = msgpack.unpack(response.raw, object_hook=decode_hook)
        return data
        
    def request_path(self, path):
        """
        Request the msgpack representation of a file or directory from the server
        """
        url = f"{self.server}/msgpack/{path}"
        return self.get_and_unpack(url)
    
    def request_object(self, path, name, data_size_limit, max_depth):
        """
        Request the msgpack representation of a HDF5 object from the server        
        """
        params = {
            "object" : name,
            "data_size_limit" : data_size_limit,
            "max_depth" : max_depth
        }
        url = f"{self.server}/msgpack/{path}"
        return self.get_and_unpack(url, params)

    def request_slice(self, path, name, start, count):
        """
        Request a dataset slice.  May return fewer elements
        than requested if result is too large for a msgpack bin
        object.
        """        
        params = {
            "object" : name,
            "start"  : ",".join([str(int(i)) for i in start]),
            "count"  : ",".join([str(int(i)) for i in count]),
            }
        url = f"{self.server}/msgpack/{path}"
        return self.get_and_unpack(url, params)

    def open_file(self, path, mode='r'):
        """
        Open the file at the specified virtual path
        """
        url = f"{self.server}/download/{path}"
        response = self.session.get(url, stream=True, verify=verify_cert)
        raise_for_status(response)
        response.raw.read = functools.partial(response.raw.read, decode_content=True)
        if mode == 'rb':
            # Binary mode
            return response.raw
        elif mode == 'r':
            # Text mode, so we need to decode bytes to strings
            return codecs.getreader(response.encoding)(response.raw)
        else:
            raise ValueError("File mode must be 'r' (text) or 'rb' (binary)")

