#!/usr/bin/python3
"""Unit tests for the FileStorage class."""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """Defines test cases for the FileStorage class."""

    def setUp(self):
        """Initialize test environment."""
        pass

    def reset_storage(self):
        """Clear FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Clean up test environment."""
        self.reset_storage()
        pass

    def test_instance_creation(self):
        """Test that storage is an instance of FileStorage."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_no_arguments(self):
        """Test __init__ with no parameters."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        self.assertEqual(str(e.exception), "descriptor '__init__' of 'object' object needs an argument")

    def test_init_with_arguments(self):
        """Test __init__ with excessive parameters."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(str(e.exception), "object() takes no parameters")

    def test_class_attributes(self):
        """Test the attributes of the FileStorage class."""
        self.reset_storage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def helper_test_all(self, classname):
        """Helper to test all() method for a given class."""
        self.reset_storage()
        self.assertEqual(storage.all(), {})

        obj = storage.classes()[classname]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_all_base_model(self):
        """Test all() method for BaseModel."""
        self.helper_test_all("BaseModel")

    def test_all_user(self):
        """Test all() method for User."""
        self.helper_test_all("User")

    def test_all_state(self):
        """Test all() method for State."""
        self.helper_test_all("State")

    def test_all_city(self):
        """Test all() method for City."""
        self.helper_test_all("City")

    def test_all_amenity(self):
        """Test all() method for Amenity."""
        self.helper_test_all("Amenity")

    def test_all_place(self):
        """Test all() method for Place."""
        self.helper_test_all("Place")

    def test_all_review(self):
        """Test all() method for Review."""
        self.helper_test_all("Review")

    def helper_test_all_multiple(self, classname):
        """Helper to test all() method with multiple objects."""
        self.reset_storage()
        self.assertEqual(storage.all(), {})

        cls = storage.classes()[classname]
        objs = [cls() for _ in range(1000)]
        [storage.new(o) for o in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for o in objs:
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertIn(key, storage.all())
            self.assertEqual(storage.all()[key], o)

    def test_all_multiple_base_model(self):
        """Test all() method with multiple BaseModel objects."""
        self.helper_test_all_multiple("BaseModel")

    def test_all_multiple_user(self):
        """Test all() method with multiple User objects."""
        self.helper_test_all_multiple("User")

    def test_all_multiple_state(self):
        """Test all() method with multiple State objects."""
        self.helper_test_all_multiple("State")

    def test_all_multiple_city(self):
        """Test all() method with multiple City objects."""
        self.helper_test_all_multiple("City")

    def test_all_multiple_amenity(self):
        """Test all() method with multiple Amenity objects."""
        self.helper_test_all_multiple("Amenity")

    def test_all_multiple_place(self):
        """Test all() method with multiple Place objects."""
        self.helper_test_all_multiple("Place")

    def test_all_multiple_review(self):
        """Test all() method with multiple Review objects."""
        self.helper_test_all_multiple("Review")

    def test_all_no_arguments(self):
        """Test all() with no parameters."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        self.assertEqual(str(e.exception), "all() missing 1 required positional argument: 'self'")

    def test_all_excessive_arguments(self):
        """Test all() with excessive parameters."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 98)
        self.assertEqual(str(e.exception), "all() takes 1 positional argument but 2 were given")

    def helper_test_new(self, classname):
        """Helper to test new() method for a given class."""
        self.reset_storage()
        cls = storage.classes()[classname]
        obj = cls()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], obj)

    def test_new_base_model(self):
        """Test new() method for BaseModel."""
        self.helper_test_new("BaseModel")

    def test_new_user(self):
        """Test new() method for User."""
        self.helper_test_new("User")

    def test_new_state(self):
        """Test new() method for State."""
        self.helper_test_new("State")

    def test_new_city(self):
        """Test new() method for City."""
        self.helper_test_new("City")

    def test_new_amenity(self):
        """Test new() method for Amenity."""
        self.helper_test_new("Amenity")

    def test_new_place(self):
        """Test new() method for Place."""
        self.helper_test_new("Place")

    def test_new_review(self):
        """Test new() method for Review."""
        self.helper_test_new("Review")

    def test_new_no_arguments(self):
        """Test new() with no parameters."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            storage.new()
        self.assertEqual(str(e.exception), "new() missing 1 required positional argument: 'obj'")

    def test_new_excessive_arguments(self):
        """Test new() with excessive parameters."""
        self.reset_storage()
        obj = BaseModel()
        with self.assertRaises(TypeError) as e:
            storage.new(obj, 98)
        self.assertEqual(str(e.exception), "new() takes 2 positional arguments but 3 were given")

    def helper_test_save(self, classname):
        """Helper to test save() method for a given class."""
        self.reset_storage()
        cls = storage.classes()[classname]
        obj = cls()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        data = {key: obj.to_dict()}
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as file:
            self.assertEqual(len(file.read()), len(json.dumps(data)))
            file.seek(0)
            self.assertEqual(json.load(file), data)

    def test_save_base_model(self):
        """Test save() method for BaseModel."""
        self.helper_test_save("BaseModel")

    def test_save_user(self):
        """Test save() method for User."""
        self.helper_test_save("User")

    def test_save_state(self):
        """Test save() method for State."""
        self.helper_test_save("State")

    def test_save_city(self):
        """Test save() method for City."""
        self.helper_test_save("City")

    def test_save_amenity(self):
        """Test save() method for Amenity."""
        self.helper_test_save("Amenity")

    def test_save_place(self):
        """Test save() method for Place."""
        self.helper_test_save("Place")

    def test_save_review(self):
        """Test save() method for Review."""
        self.helper_test_save("Review")

    def test_save_no_arguments(self):
        """Test save() with no parameters."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        self.assertEqual(str(e.exception), "save() missing 1 required positional argument: 'self'")

    def test_save_excessive_arguments(self):
        """Test save() with excessive parameters."""
        self.reset_storage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        self.assertEqual(str(e.exception), "save() takes 1 positional argument but 2 were given")

    def helper_test_reload(self, classname):
        """Helper to test reload() method for a given class."""
        self.reset_storage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        cls = storage.classes
