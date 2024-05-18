#!/usr/bin/python3
"""
defines all common attributes/methods for Amenity.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines all common attributes/methods for Amenity,
    while inheriting from the `BaseModel` class.
    """
    name = ""
