#!/usr/bin/python3
"""
defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    defines all common attributes/methods for other classes.

    Attributes:
        id (str):               assigned with an uuid when
                                    an instance is created
        created_at (datetime):     assign with the current datetime when
                                    an instance is created.
        updated_at (datetime):     assign with the current datetime
                                    when an instance is created.  It will
                                    be updated every time you change the object
    Methods:
        save(self):     updates the public instance attribute `updated_at`
                        with the current datetime
        to_dict(self):  returns a dictionary containing all keys/values of
                        `__dict__` of the instance
    """
    TIME_FORM = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel instance.

        Arguments:
            kwargs:             to re-create an instance with a `dict`
                                representation.
        Attributes:
        id (str):               assigned with an uuid when
                                    an instance is created
        created_at (datetime):     assign with the current datetime when
                                    an instance is created.
        updated_at (datetime):     assign with the current datetime
                                    when an instance is created.  It will
                                    be updated every time you change the object

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, self.TIME_FORM)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string represnetation of the BaseModel instance.

        Returns:
            str:    A string containing the class name, ID,
                    and dictionary representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute `updated_at` with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        `__dict__` of the instance.

        Returns:
            dict: A dictionary containing all keys/values of
            `__dict__` of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()
        return dictionary
