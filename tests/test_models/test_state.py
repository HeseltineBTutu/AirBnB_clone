import unittest
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_name(self):
        self.assertEqual(self.state.name, "")
