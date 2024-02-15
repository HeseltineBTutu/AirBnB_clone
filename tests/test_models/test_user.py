import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_email(self):
        self.assertEqual(self.user.email, "")

    def test_password(self):
        self.assertEqual(self.user.password, "")

    def test_firs_name(self):
        self.assertEqual(self.user.first_name, "")

    def test_default_last_name(self):
        self.assertEqual(self.user.last_name, "")

if __name__ == "__main__":
    unittest.main()
