"""
Module defining the Amenity class

This module contains the definition of the Amenity class,
which represent a city in some context
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Class definition of Amenity.

    Attributes:
        name (str): The name of the amenity

    """
    name = ""
