#!/usr/bin/env python3
"""
test_client.py

contains the tests for the functions/classes contained in the
client.py file
"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
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
        reference = GithubOrgClient(org_name)
        reference.org()

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name)
        )

    def test_public_repos_url(self):
        """test_public_repos_url() test method"""
        payload = {
            'login': 'google',
            'id': 1342004,
            'node_id': 'MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=',
            'url': 'https://api.github.com/orgs/google',
            'repos_url': 'https://api.github.com/orgs/google/repos',
            'events_url': 'https://api.github.com/orgs/google/events',
            'hooks_url': 'https://api.github.com/orgs/google/hooks',
            'issues_url': 'https://api.github.com/orgs/google/issues'
          }
        context = 'client.GithubOrgClient.org'
        with patch(context, new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            reference = GithubOrgClient('google')
            self.assertEqual(reference._public_repos_url, payload['repos_url'])
