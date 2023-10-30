#!/usr/bin/env python3
"""
test_client.py

contains the tests for the functions/classes contained in the
client.py file
"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    test case: Testing the GithubOrgClient class defined in client.py
    """
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org test method"""
        # mock_get_json.return_value = Mock(return_value={'org_name': org_name})
        reference = GithubOrgClient(org_name)
        reference.org()

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )
