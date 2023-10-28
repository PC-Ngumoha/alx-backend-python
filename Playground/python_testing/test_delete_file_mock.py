#!/usr/bin/env python
# -*- coding: utf-8 -*-

from delete_file import rm

from unittest import mock
import unittest

class RmTestCase(unittest.TestCase):
    
    @mock.patch('delete_file.os.path')
    @mock.patch('delete_file.os')
    def test_rm(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        rm('a path')
        self.assertFalse(mock_os.remove.called, 'Failed to remove the file if not present')
        mock_path.isfile.return_value = True
        rm('a path')
        mock_os.remove.assert_called_with('a path')
