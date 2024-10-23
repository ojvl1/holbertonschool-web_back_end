#!/usr/bin/env python3
"""
Test Cases
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up the class for integration tests"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = cls.mock_requests

    @classmethod
    def tearDownClass(cls):
        """Tear down the class for integration tests"""
        cls.get_patcher.stop()

    @classmethod
    def mock_requests(cls, url):
        """Mock requests.get() behavior"""
        if url == f"https: //api.github.com/orgs/{
                    cls.org_payload['login']}":
            return cls.create_mock_response(cls.org_payload)
        elif url == cls.org_payload['repos_url']:
            return cls.create_mock_response(cls.repos_payload)
        raise ValueError("Unhandled URL")

    @staticmethod
    def create_mock_response(payload):
        """Create a mock response object"""
        mock_response = patch('requests.Response')
        mock_response.json.return_value = payload
        return mock_response

    def test_public_repos(self):
        """Test public_repos returns expected repository names"""
        client = GithubOrgClient(self.org_payload['login'])
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)


if __name__ == '__main__':
    unittest.main()
