"""
Module defining the City class.

This module contains the definition of the City class
which represents a city
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Class definition of a city

    Attributes:
        state_id (str): The ID of the state associated with the city.
                        It is initially an empty string and will be set to the State's ID.
        name (str): The name of the City
    """
    state_id = ""
    name = ""
