import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_city_id(self):
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        self.assertEqual(self.place.name, "")

    def test_description(self):
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        self.assertEqual(self.place.amenity_ids, [])
