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

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

if __name__ == '__main__':
    unittest.main()