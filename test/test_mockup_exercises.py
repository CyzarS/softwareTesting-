import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch, mock_open
import subprocess

from mockup_exercises import (
    fetch_data_from_api,
    read_data_from_file,
    execute_command,
    perform_action_based_on_time,
)

class TestMockupFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_data_from_api(self, mock_get):
        # Mock the response of requests.get
        mock_get.return_value.json.return_value = {"message": "success"}
        url = "https://fakeapi.com"
        result = fetch_data_from_api(url)
        self.assertEqual(result, {"message": "success"})
        mock_get.assert_called_with(url, timeout=10)

    @patch("builtins.open", new_callable=mock_open, read_data="Hello World")
    def test_read_data_from_file(self, mock_file):
        result = read_data_from_file("file.txt")
        self.assertEqual(result, "Hello World")
        mock_file.assert_called_once_with("file.txt", encoding="utf-8")

    def test_read_data_from_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("nonexistent.txt")

    @patch("subprocess.run")
    def test_execute_command_success(self, mock_run):
        mock_run.return_value = subprocess.CompletedProcess(
            args=["echo", "Hello"], returncode=0, stdout="Hello\n"
        )
        result = execute_command(["echo", "Hello"])
        self.assertEqual(result, "Hello\n")
        mock_run.assert_called_once()

    @patch("time.time", return_value=5)
    def test_perform_action_based_on_time_before_10(self, mock_time):
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch("time.time", return_value=15)
    def test_perform_action_based_on_time_after_10(self, mock_time):
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")

if __name__ == "__main__":
    unittest.main()