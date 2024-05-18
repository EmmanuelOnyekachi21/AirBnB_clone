#!/usr/bin/python3
"""
defines all common attributes/methods for Review.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines all common attributes/methods for Review,
    while inheriting from the `BaseModel` class.
    """
    place_id = ""
    user_id = ""
    text = ""
