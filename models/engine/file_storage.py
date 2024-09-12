#!/usr/bin/python3
"""
Hekolfnd
"""


import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    kfmkfm
    """
    __file_path = "file.json"
    __objects = {}

    models = {
            'BaseModel': BaseModel,
            }

    def all(self):
        """
        all
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new
        """

        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj
        
    def save(self):
        """
        save
        """
        new_dict = (
                {key: val.to_dict()
                 for key, val in FileStorage.__objects.items()
                 })

        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        re
        """
        if (
                (os.path.exists(FileStorage.__file_path)) and
                (os.path.getsize(FileStorage.__file_path) > 0)
                ):
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)

            for key, val in data.items():
                class_name = key.split('.')[0]
                cls = FileStorage.models[class_name]
                obj = cls(**val)
                FileStorage.__objects[key] = obj
