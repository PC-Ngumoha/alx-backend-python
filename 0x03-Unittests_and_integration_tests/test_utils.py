#!/usr/bin/env python3
"""
test_utils.py

contains the tests for the functions in the utils.py file
defined in the current directory
"""
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
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


class TestGetJson(unittest.TestCase):
    """
    test case: Testing the function of the get_json() function
    """
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    @patch('utils.requests.get', autospec=True)
    def test_get_json(self, test_url, test_payload, mock_request_get):
        """test_get_json() test method"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_request_get.return_value = mock_response

        output = get_json(test_url)
        mock_request_get.assert_called_with(test_url)
        self.assertEqual(output, test_payload)


class TestMemoize(unittest.TestCase):
    """
    test case: Testing the utils.memoize decorator
    """
    def test_memoize(self):
        """test_memoize() test method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_obj = TestClass()
            test_obj.a_property()
            test_obj.a_property()

            mock_a_method.assert_called_once()
