#!/bin/env python

import collections.abc

from hdfstream.connection import Connection
from hdfstream.remote_file import RemoteFile
from hdfstream.remote_group import RemoteGroup
from hdfstream.remote_dataset import RemoteDataset
from hdfstream.defaults import *


class RemoteDirectory(collections.abc.Mapping):
    """
    Object representing a virtual directory on the remote server
    """
    def __init__(self, server, name, user=None, password=None, data=None,
                 max_depth=max_depth_default, data_size_limit=data_size_limit_default,
                 lazy_load=False, connection=None):

        # Remove any trailing slashes from the directory name
        name = name.rstrip("/")
        
        # Set up a new session if necessary. May need to ask for password.
        if connection is None:
            connection = Connection.new(server, user, password)
        self.connection = connection

        # Store parameters
        self.data_size_limit = data_size_limit
        self.max_depth = max_depth
        self.name = name
        self.unpacked = False
        
        # If msgpack data was supplied, decode it. If not, we'll wait until
        # we actually need the data before we request it from the server.
        if data is not None:
            self.unpack(data)

        # If the class was explicitly instantiated by the user (and not by a
        # recursive unpack() call) then we should always contact the server so
        # that we immediately detect incorrect paths.
        if lazy_load==False and not(self.unpacked):
            self.load()
            
    def load(self):
        """
        Request the msgpack representation of this directory from the server
        """
        if not self.unpacked:
            data = self.connection.request_path(self.name)
            self.unpack(data)
            
    def unpack(self, data):
        """
        Decode the msgpack representation of this directory
        """        
        # Store dict of files in this directory
        self._files = {}
        for filename, filedata in data["files"].items():
            file_path = self.name + "/" + filename
            self._files[filename] = RemoteFile(self.connection, file_path, max_depth=self.max_depth,
                                               data_size_limit=self.data_size_limit, data=filedata)
            
        # Store dict of subdirectories in this directory
        self._directories = {}
        for subdir_name, subdir_data in data["directories"].items():
            subdir_object = RemoteDirectory(self.connection.server, self.name+"/"+subdir_name, data=subdir_data, lazy_load=True,
                                            connection=self.connection)
            self._directories[subdir_name] = subdir_object
        self.unpacked = True
            
    def __getitem__(self, key):

        # Request directory listing from the server if necessary
        self.load()

        # Remove any trailing slash
        if key != "/":
            key = key.rstrip("/")
        
        # Check for the case where key refers to something in a sub-directory
        components = key.split("/", 1)
        if len(components) > 1:
            return self._directories[components[0]][components[1]]

        # Check if key refers to a subdirectory in this directory
        name = components[0]
        if name in self._directories:
            return self._directories[name]
        
        # Check if key refers to a file in this directory
        if name in self._files:
            return self._files[name]

        raise KeyError("Invalid path: "+key)
        
    def __len__(self):
        self.load()
        return len(self._directories) + len(self._files)

    def __iter__(self):
        self.load()
        for directory in self._directories:
            yield directory
        for file in self._files:
            yield file

    def __repr__(self):
        self.load()
        nr_files = len(self._files)
        nr_dirs = len(self._directories)
        return f'<Remote directory {self.name} with {nr_dirs} sub-directories, {nr_files} files>'

    @property
    def files(self):
        self.load()
        return self._files

    @property
    def directories(self):
        self.load()
        return self._directories
