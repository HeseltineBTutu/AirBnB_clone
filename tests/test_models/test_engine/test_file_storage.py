import unittest
import json
import os
from unittest.mock import patch, MagicMock
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        # Clear any saved objects between tests
        if os.path.exists("file.json"):
            os.remove("file.json")

    @patch("models.engine.file_storage.os.path.exists")
    def test_reload_empty_file(self, mock_exists):
        self.storage.reload()

        self.assertEqual({}, self.storage.all())

    @patch("models.engine.file_storage.open", create=True)
    @patch("os.path.exists", return_value=True)
    def test_reload_with_invalid_json(self, mock_exists, mock_open):
        mock_file = MagicMock()
        mock_file.read.return_value = "invalid json"
        mock_open.return_value.__enter__.return_value = mock_file

        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()

    @patch("models.engine.file_storage.open", create=True)
    @patch("os.path.exists", return_value=True)
    def test_reload_with_existing_file(self, mock_exists, mock_open):
        mock_file = MagicMock()
        mock_file.read.return_value = '{"BaseModel.1": {"id": 1, "name": "Alice"}}'
        mock_open.return_value.__enter__.return_value = mock_file

        self.storage.reload()

        expected_data = {"BaseModel.1": {"id": 1, "name": "Alice"}}
        self.assertEqual(expected_data, self.storage.all())

    def test_new_object_stored(self):
        obj = BaseModel(name="Bob")
        self.storage.new(obj)
        expected_key = f"{obj.__class__.__name__}.{obj.id}"
        all_objects = self.storage.all()
        self.assertTrue(expected_key in all_objects)
        self.assertTrue(expected_key in all_objects)

    def test_save_serializes_objects(self):
        obj = BaseModel(name="Charlie")
        self.storage.new(obj)
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        expected_key = f"{obj.__class__.__name__}.{obj.id}"
        expected_dict = {expected_key: obj.to_dict()}
        self.maxDiff = None
        self.assertEqual(expected_dict, data)

    def test_all_returns_empty_dict_if_no_object(self):
        self.assertEqual({}, self.storage.all())

if __name__ == "__main__":
    unittest.main()
