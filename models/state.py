#!/usr/bin/python3
"""
State Module: This module defines all common attributes/methods for State.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class: Defines all common attributes/methods for State,
    while inheriting from the `BaseModel` class.
    """
    name = ""
