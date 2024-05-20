#!/usr/bin/python3
"""
    Amenity Modules: defines all common attributes/methods for Amenity.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class: Defines all common attributes/methods for Amenity,
    while inheriting from the `BaseModel` class.
    """
    name = ""
