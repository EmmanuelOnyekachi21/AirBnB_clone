#!/usr/bin/python3
"""
Models.user
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
