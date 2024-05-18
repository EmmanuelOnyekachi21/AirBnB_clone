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
    Serializes instances to a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects by <class name>.id.
        models (dict): Mapping of class names to classes for deserialization.
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
        Returns the dictionary `__objects` which contains all stored objects.

        Returns:
            dict: A dictionary of all stored objects with keys as
            <class name>.id and values as the object instances.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: The object to be stored.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file specified by __file_path.

        The method converts each object to its dictionary representation
        using the `to_dict` method and then writes the serialized data to
        the JSON file.
        """
        objects = {}

        for key, value in self.__objects.items():
            objects[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(objects, file, indent=2)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the file exists.

        If the JSON file specified by __file_path exists and is not empty,
        it reads the file, converts the JSON data back to objects using the
        class mappings in `models`, and stores them in __objects.
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
