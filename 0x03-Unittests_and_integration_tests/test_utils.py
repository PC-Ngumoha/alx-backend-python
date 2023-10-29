#!/usr/bin/env python3
"""
test_utils.py

contains the tests for the functions in the utils.py file
defined in the current directory
"""
from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    test case: Testing the access_nested_map() function
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, map, path):
        """test_access_nested_map_exception test function"""
        with self.assertRaises(KeyError):
            access_nested_map(map, path)
