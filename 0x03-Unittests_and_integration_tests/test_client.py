#!/usr/bin/env python3
"""
test_client.py

contains the tests for the functions/classes contained in the
client.py file
"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD as test_payload
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
import utils
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

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """test_public_repos() test method"""
        payload = [
            {
                'id': 1936771,
                'node_id': 'MDEwOlJlcG9zaXRvcnkxOTM2Nzcx',
                'name': 'truth',
                'full_name': 'google/truth',
            },
            {
                'id': 1936772,
                'node_id': 'MDEwOlJlcG9zaXRvcnkxOTM2Nzcx',
                'name': 'ruby-openid-apps-discovery',
                'full_name': 'google/open',
            },
            {
                'id': 1936773,
                'node_id': 'MDEwOlJlcG9zaXRvcnkxOTM2Nzcx',
                'name': 'autoparse',
                'full_name': 'google/autoparse',
            },
            {
                'id': 1936774,
                'node_id': 'MDEwOlJlcG9zaXRvcnkxOTM2Nzcx',
                'name': 'anvil-build',
                'full_name': 'google/anvil',
            }
        ]
        result = ['truth', 'ruby-openid-apps-discovery',
                  'autoparse', 'anvil-build']
        context = 'client.GithubOrgClient._public_repos_url'
        with patch(context, new_callable=PropertyMock) as mocked_repos_url:
            mocked_repos_url.return_value =\
              'https://api.github.com/orgs/google/repos'
            mocked_get_json.return_value = payload
            reference = GithubOrgClient('google')
            repo_list = reference.public_repos()
            self.assertEqual(repo_list, result)
            mocked_repos_url.assert_called_once()
            mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """test_has_license() test method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    test_payload
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test: Testing the GithubOrgClient class
    """
    @classmethod
    def setUpClass(cls):
        """set up the class"""
        cls.get_patcher = patch('requests.get',
                                side_effect=cls.side_effect,
                                return_value=None)
        cls.mock_request_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """tearing down the class"""
        cls.get_patcher.stop()

    @classmethod
    def side_effect(cls, url):
        """get_url_fixtures() side effect method"""
        mock_response = Mock()
        if url.endswith('/google'):
            mock_response.json.return_value = cls.org_payload
            return mock_response
        elif url.endswith('/google/repos'):
            mock_response.json.return_value = cls.repos_payload
            return mock_response
        else:
            return DEFAULT
