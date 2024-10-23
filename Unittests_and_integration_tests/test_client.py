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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repos"""

        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=unittest.mock.PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/test_org/repos"
            )

            client = GithubOrgClient("test_org")

            result = client.public_repos()

            expected_repos = ["repo1", "repo2", "repo3"]

            self.assertEqual(result, expected_repos)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the expected value"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
