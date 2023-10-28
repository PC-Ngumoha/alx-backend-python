#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import os.path


class RemovalService:
    """
    Service for removing objects from a file system.
    """

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)


class UploadService:
    """
    Service for uploading objects to a file system.
    """
    def __init__(self, removal_service):
        """__init__() method"""
        self.removal_service = removal_service

    def upload_complete(self, filename):
        """upload_complete() method"""
        self.removal_service.rm(filename)
