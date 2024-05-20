#!/usr/bin/python3
"""Unit test module for the Amenity Class."""

import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity class."""

    def setUp(self):
        """Set up resources required for testing."""
        self.reset_storage()

    def tearDown(self):
        """Clean up after tests."""
        self.reset_storage()

    def reset_storage(self):
        """Clear the storage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Test if Amenity instances are correctly instantiated."""
        instance = Amenity()
        self.assertEqual(str(type(instance)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(instance, Amenity)
        self.assertTrue(issubclass(type(instance), BaseModel))


if __name__ == "__main__":
    unittest.main()
