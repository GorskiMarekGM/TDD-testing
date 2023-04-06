import pathlib
import unittest
from unittest import mock
from src.todo.db import BasicDB

class TestBasicDB(unittest.TestCase):
    def test_load(self):
        mock_file = mock.MagicMock(
            read = mock.Mock(return_value='["first","second]')
        )
        mock_file.__enter__.return_value = mock_file
        mock_opener = mock.Mock