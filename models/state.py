"""
Module defining the State class.

This module contains the definition of the State class,
which represents a state in some context.
"""
from .base_model import BaseModel

class State(BaseModel):
    """
    Class definition of state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
