#!/usr/bin/python3
"""
City Module: defines all common attributes/methods for City.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class: Defines all common attributes/methods for City,
    while inheriting from the `BaseModel` class.
    """
    state_id = ""
    name = ""
