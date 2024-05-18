#!/usr/bin/python3
"""
This module defines the FileStorage class, which serializes instances
to a JSON file and deserializes JSON file to instances.
"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    models = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
        }

    def all(self):
        """
        Returns the dictionary `__objects`
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        objects = {}

        for key, value in self.__objects.items():
            objects[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(objects, file, indent=2)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.)
        """
        if (
                (os.path.exists(self.__file_path)) and
                (os.path.getsize(self.__file_path) > 0)):
            with open(self.__file_path, "r") as file:
                data = json.load(file)

                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = self.models[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
