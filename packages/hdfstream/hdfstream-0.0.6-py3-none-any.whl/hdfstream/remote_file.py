#!/bin/env python

import collections.abc
from hdfstream.remote_group import RemoteGroup
from hdfstream.defaults import *
from hdfstream.exceptions import *


class RemoteFile(collections.abc.Mapping):
    """
    Object representing a file on the remote server
    """
    def __init__(self, connection, file_path, max_depth=max_depth_default,
                 data_size_limit=data_size_limit_default, data=None):

        self.connection = connection
        self.file_path = file_path
        self.max_depth = max_depth
        self.data_size_limit = data_size_limit
        self.unpacked = False

        # If msgpack data was supplied, decode it. If not, we'll wait until
        # we actually need the data before we request it from the server.
        if data is not None:
            self.unpack(data)

        self._root = None
            
    def load(self):
        """
        Request the msgpack representation of this file from the server
        """
        if not self.unpacked:
            data = self.connection.request_path(self.file_path)
            self.unpack(data)
            
    def unpack(self, data):
        """
        Decode the msgpack representation of this group
        """
        self.media_type = str(data["type"])
        self.size = int(data["size"])
        self.last_modified = int(data["last_modified"])
        self.unpacked = True

    @property
    def root(self):
        """
        Open the HDF5 root group in this file, if we didn't already
        """
        if self._root is None:
            if self.media_type != "application/x-hdf5":
                raise HDFStreamRequestError("Cannot open non-HDF5 file as HDF5!")
            self.load()
            self._root = RemoteGroup(self.connection, self.file_path, name="/",
                                     max_depth=self.max_depth,
                                     data_size_limit=self.data_size_limit)
        return self._root

    def open(self, mode='r'):
        """
        Return a File-like object with the contents of the file

        Reading returns bytes if mode='rb' or strings if mode='r'.
        """
        return self.connection.open_file(self.file_path, mode=mode)
        
    def __getitem__(self, key):
        return self.root.__getitem__(key)
        
    def __len__(self):
        return self.root.__len__()
        
    def __iter__(self):
        for member in self.root:
            yield member

    def __repr__(self):
        return f'<Remote file "{self.file_path}">'
