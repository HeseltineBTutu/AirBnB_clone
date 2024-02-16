"""
Module defining the Review class.

This module contains the definition of the Review class,
which represents a review associated with a place and a user.
"""
from .base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
