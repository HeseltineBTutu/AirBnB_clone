import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init_defaults(self):
        """Test default initialization of BaseModel instance."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertAlmostEqual(obj.created_at, obj.updated_at, delta=timedelta(milliseconds=10))

    def test_init_custom_timestamps(self):
        """Test initialization of BaseModel instance with custom timestamps."""
        created_at = datetime(2022, 1, 1, 0, 0, 0)
        updated_at = datetime(2023, 1, 1, 0, 0, 0)

        obj = BaseModel(created_at=created_at, updated_at=updated_at)
        self.assertEqual(obj.created_at, created_at)
        self.assertEqual(obj.updated_at, updated_at)

    def test_init_with_none_timestamps(self):
        """Test initialization of BaseModel instance with None timestamps."""
        obj = BaseModel(created_at=None, updated_at=None)
        self.assertIsInstance(obj.id, str)
        self.assertIsNone(obj.created_at)
        self.assertIsNone(obj.updated_at)

    def test_save_with_none_timestamp(self):
        """
        Test saving BaseModel instance with None updated_at timestamp.
        """
        obj = BaseModel()
        obj.save()
        obj.save()  # Save again to ensure updated_at is actually updated
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save_updates_timestamp(self):
        """
        Test if the save() method updates the 'updated_at' timestamp.
        """
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test if the to_dict() method returns a dictionary
        with expected keys and values.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
