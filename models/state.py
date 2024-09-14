#!/usr/bin/python3
"""State class definition"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attribute:
        name (str): Name of state.
    """

    name = ""
