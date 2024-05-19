#!/usr/bin/python3
"""
defines all common attributes/methods for State.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    Defines all common attributes/methods for State,
    while inheriting from the `BaseModel` class.
    """
    name = ""
