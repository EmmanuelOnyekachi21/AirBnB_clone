#!/usr/bin/python3
"""
User Module: defines all common attributes/methods for User.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class: Defines all common attributes/methods for User,
    while inheriting from the `BaseModel` class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
