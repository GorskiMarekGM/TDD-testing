import queue
import unittest
import threading
import tempfile
import pathlib
from src.todo.app import TODOApp
from src.todo.db import BasicDB


class TestTODOAcceptance(unittest.TestCase):
    def setUp(self):
        self.inputs = queue.Queue()
        self.outputs = queue.Queue()

        self.fake_output = lambda txt: self.outputs.put(txt)
        self.fake_input = lambda: self.inputs.get()
        self.get_output = lambda: self.outputs.get(timeout=1)
        self.send_input = lambda cmd: self.inputs.put(cmd)

    def test_main(self):
        app = TODOApp(io=(self.fake_input, self.fake_output))

        # https://realpython.com/intro-to-python-threading/ o threadingu
        app_thread = threading.Thread(target=app.run, daemon=True)
        app_thread.start()

        # ...

        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"+
            "\n"+
            "\n"+
            "> "
        ))
        self.send_input("add kupic mleko")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"
            "1. kupic mleko\n"
            "\n"
            "> "
        ))

        self.send_input("add kupic jajka")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"
            "1. kupic mleko\n"
            "2. kupic jajka\n"
            "\n"
            "> "
        ))
        self.send_input("del 1")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"
            "1. kupic jajka\n"
            "\n"
            "> "
        ))
        self.send_input("quit")
        app_thread.join(timeout=1)
        self.assertEqual(self.get_output(), "Żegnaj!\n")

    def test_persistence(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            app_thread = threading.Thread(
                target=TODOApp(
                io=(self.fake_input, self.fake_output),
                dbmanager=BasicDB(pathlib.Path(tmpdirname, "db"))
                ).run,
                daemon=True
            )
            app_thread.start()

            welcome = self.get_output()
            self.assertEqual(welcome,(
            "Lista rzeczy do zrobienia:\n"+
            "\n"+
            "\n"+
            "> "
            ))

            self.send_input("add kupić mleko")
            self.send_input("quit")
            app_thread.join(timeout=1)

            while True:
                try:
                    self.get_output()
                except queue.Empty:
                    break
            app_thread = threading.Thread(
                target=TODOApp(
                io=(self.fake_input, self.fake_output)
                ).run,
                daemon=True
            )
            app_thread.start()

            welcome = self.get_output()
            self.assertEqual(
                welcome, (
                "Lista rzeczy do zrobienia:\n"
                "1. kupic mleko\n"
                "\n"
                "> "
                )
            )
            self.send_input("quit")
            app_thread.join(timeout=1)



            
