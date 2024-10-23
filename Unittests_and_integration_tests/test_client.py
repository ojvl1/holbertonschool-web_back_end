#!/usr/bin/env python3
"""
Test Cases
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_response, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = mock_response

        client = GithubOrgClient(org_name)

        self.assertEqual(client.org, mock_response)

        mock_get_json.assert_called_once_with(
            f"https: //api.github.com/orgs/{org_name}"
        )


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class"""

    def test_public_repos_url(self):
        """Test _public_repos_url returns
        the correct URL based on org payload"""
        with patch('client.GithubOrgClient.org',
                   new_callable=unittest.mock.PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test_org/repos"}

            client = GithubOrgClient("test_org")

            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/test_org/repos")

            mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()
