#!/usr/bin/python3
"""Unit test module for the City Class."""

import unittest
from models.city import City
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test suite for the City class."""

    def setUp(self):
        """Prepare resources before each test."""
        self.reset_storage()

    def tearDown(self):
        """Clean up resources after each test."""
        self.reset_storage()

    def reset_storage(self):
        """Reset the storage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Test City class instantiation."""
        instance = City()
        self.assertEqual(str(type(instance)), "<class 'models.city.City'>")
        self.assertIsInstance(instance, City)
        self.assertTrue(issubclass(type(instance), BaseModel))


if __name__ == "__main__":
    unittest.main()

