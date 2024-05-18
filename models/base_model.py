#!/usr/bin/python3
"""
    BaseModel for creating every single attributes
    that will be inherited for all objects
"""


import uuid
from datetime import datetime


class BaseModel:
    """
        this is for object creation.
    """
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, **kwargs):
        """
            init function
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, self.TIME_FORMAT)
                if key != '__class__':
                    setattr(self, key, value)

        else:
            import models
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """
            str function
        """
        obj_str = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
        return obj_str

    def save(self):
        """
            save method
        """
        import models
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """
            dic method
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        for k, v in obj_dict.items():
            if isinstance(v, datetime):
                obj_dict[k] = v.isoformat()

        return obj_dict
