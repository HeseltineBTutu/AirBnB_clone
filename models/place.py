"""
Module defining the Place class

This module contains the definitions of the Place class,
which represents a place or accommodation.
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    Class definition of Place or accomodation.

    Attributes:
        city_id (str): The ID of the city associated with the place.
        user_id (str): The ID of the user associated with the place.
        name (str): The name of the place
        description (str): The description of the place.
        number_rooms (int): The number of room in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guest allowed in the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of IDs of amenities associated with the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
