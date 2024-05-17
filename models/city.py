#!/usr/bin/python3
"""
defines all common attributes/methods for City.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines all common attributes/methods for City,
    while inheriting from the `BaseModel` class.
    """
    state_id = ""
    name = ""
