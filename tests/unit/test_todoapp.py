import unittest
import tempfile
from pathlib import Path
from src.todo.app import TODOApp
from unittest.mock import Mock

class TestTODOApp(unittest.TestCase):
    # def test_default_dbpath(self):
    #     app = TODOApp()
    #     assert Path(".").resolve() == Path(app._dbpath).resolve()

    # def test_accepts_dbpath(self):
    #     expected_path = Path(tempfile.gettempdir(), "cokolwiek")
    #     app = TODOApp(dbpath=str(expected_path))
    #     assert expected_path == Path(app._dbpath)

    def test_noloader(self):
        app = TODOApp(io=(Mock(return_value="quit"), Mock()),dbmanager=None)
        app.run()

        assert app._entries == []

    def test_load(self):
        dbmanager = Mock(load = Mock(
            return_value=["kupić mleko", "kupić wodę"]
        ))
        app = TODOApp(io=(Mock(return_value="quit"), Mock()), dbmanager=dbmanager)
        app.run()

        dbmanager.load.assert_called_with()
        assert app._entries == ["kupić mleko", "kupić wodę"]


