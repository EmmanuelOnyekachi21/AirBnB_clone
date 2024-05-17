#!/usr/bin/python3
"""
defines all common attributes/methods for User.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines all common attributes/methods for User,
    while inheriting from the `BaseModel` class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
