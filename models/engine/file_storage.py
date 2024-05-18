#!/usr/bin/python3
"""
    responsible for persisting object state in file_db.
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        FileStorage.
    """
    ALL_CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
    }
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj) -> None:

        """
            this adding New Object to file storage.
        """
        # construct key
        key = "{}.{}".format(
            obj.__class__.__name__, obj.id
        )
        self.__objects[key] = obj

    def all(self) -> dict:
        """
            this method is responsible for returning the whole
            object in the file __objects dictionary.
        """
        return self.__objects

    def save(self) -> None:
        """
            for converting the python objects into python dictionary,
            so they can be stored into the file storage,this process is called
            serialization.
        """
        # declare dictionary.
        serialized_obj = {}

        for k, v in self.__objects.items():
            # call the to_dict method in the basemodel
            # to represent every object to dict.
            serialized_obj[k] = v.to_dict()

        # print(serialized_obj)
        # dump into file storage
        with open(self.__file_path, "w") as obj_dic:
            json.dump(serialized_obj, obj_dic, indent=2)

    def reload(self) -> None:
        """
            responsible for reloading the object in file storage and
            dynamically create objects out of the data in the file storage
        """

        # open file
        # split the key of the dictionary
        # dynamically create classes base on the class name.
        if path.exists(self.__file_path) and\
                path.getsize(self.__file_path) > 0:
            with open(self.__file_path, "r") as db:

                file_content = json.load(db)

                for k, v in file_content.items():

                    # split the dictionary key
                    cls_name, cls_key = k.split('.')

                    # dynamically create the class object
                    # again according to the entry in db.

                    # same as doing.
                    global_class = self.ALL_CLASSES[cls_name]

                    result = global_class(**v)
                    # print(result)

                    self.__objects[k] = result
