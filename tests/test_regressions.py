import unittest
import io
from unittest import mock
from src.todo.db import BasicDB


class TestRegressions(unittest.TestCase):
    def test_os_release(self):
        fakefile = io.StringIO()
        fakefile.close = mock.Mock()
        data = ["add kupić mleko",
            "add kupić wodę",
            "quit"]
        
        dbmanager=BasicDB(None, _fileopener=mock.Mock(
                return_value=fakefile
            ))
        dbmanager.save(data)
        fakefile.seek(0)
        loaded_data = dbmanager.load()
        self.assertEqual(loaded_data, data)
