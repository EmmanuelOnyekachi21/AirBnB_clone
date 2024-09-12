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
    TIME_FORM = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Init.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, BaseModel.TIME_FORM)
                if key != '__class__':
                    setattr(self, key, value)
        else:
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
