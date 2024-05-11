import unittest
import io
import sys
import login
import flet as ft
from unittest.mock import MagicMock

class MockPage:
    def __init__(self):
        self.title = ''
        self.vertical_alignment = None
        self.theme_mode = None
        self.window_width = None
        self.window_height = None
        self.window_resizable = None

    def update(self):
        pass

    def clean(self):
        pass

    def add(self, control):
        pass

class TestLogin(unittest.TestCase):
    def test_main(self):
        # Capture stdout and stderr
        saved_stdout = sys.stdout
        saved_stderr = sys.stderr
        try:
            out = io.StringIO()
            err = io.StringIO()
            sys.stdout = out
            sys.stderr = err

            # Create a mock Page object
            page = MockPage()

            # Call the main function
            login.main(page)

            # Check if any exceptions were raised
            self.assertFalse(err.getvalue(), 'Unexpected output on stderr')

        finally:
            # Restore stdout and stderr
            sys.stdout = saved_stdout
            sys.stderr = saved_stderr

if __name__ == '__main__':
    unittest.main()