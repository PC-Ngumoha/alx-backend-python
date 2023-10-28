#!/usr/bin/env python
# -*- coding: utf-8 -*-

from delete_file_method import RemovalService, UploadService

from unittest import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):
    
    @mock.patch('delete_file.os.path')
    @mock.patch('delete_file.os')
    def test_rm(self, mock_os, mock_path):
        reference = RemovalService()

        mock_path.isfile.return_value = False
        reference.rm('a path')
        self.assertFalse(mock_os.remove.called, 'Failed to remove the file if not present')
        mock_path.isfile.return_value = True
        reference.rm('a path')
        mock_os.remove.assert_called_with('a path')


# OPTION 1: Mocking the RemovalService.rm() method
# class UploadServiceTestCase(unittest.TestCase):
#     @mock.patch.object(RemovalService, 'rm')
#     def test_upload_complete(self, mock_rm):
#         removal_service = RemovalService()
#         reference = UploadService(removal_service)

#         reference.upload_complete('A file name')

#         mock_rm.assert_called_with('A file name')

#         removal_service.rm.assert_called_with('A file name')

# OPTION 2: Creating Mock Instances
class UploadServiceTestCase(unittest.TestCase):
    def test_upload_complete(self):
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)

        reference.upload_complete('my uploaded file')

        mock_removal_service.rm.assert_called_with('my uploaded file')
