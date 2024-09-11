#!/usr/bin/python3
"""
BaseModel.
"""


import uuid
from datetime import datetime

class BaseModel:
    """
    Class.
    """
    def __init__(self):
        """
        Init.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Str
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()

        return dictionary
