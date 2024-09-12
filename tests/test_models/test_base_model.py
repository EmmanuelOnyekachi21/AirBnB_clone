"""
Tests
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):
    """
    Y
    """
    def setUp(self):
        """
        Setup
        """
        self.model = BaseModel()

    def tearDown(self):
        """
        TD
        """
        del self.model

    def test_instance_creation(self):
        """
        TIC
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        """
        test
        """
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertIn('created_at', model_dict)
        self.assertEqual(
                model_dict['created_at'], self.model.created_at.isoformat())
        self.assertIn('updated_at', model_dict)
        self.assertEqual(
                model_dict['updated_at'], self.model.updated_at.isoformat())


class TestBaseModel_Kwargs(unittest.TestCase):
    """
    IIII
    """
    def setUp(self):
        """Common setup for test cases."""
        self.model = BaseModel()

    def tearDown(self):
        """Common cleanup for test cases."""
        del self.model

    def test_init(self):
        """
        Test initialization of BaseModel instance.
        """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """
        go
        """
        string_repr = str(self.model)
        self.assertIn("[BaseModel]", string_repr)
        self.assertIn(self.model.id, string_repr)
        self.assertIn(str(self.model.__dict__), string_repr)

    def test_save(self):
        """
        Test saving functionality of BaseModel instance.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """
        Test conversion of BaseModel instance to dictionary.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(
                model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(
                model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_init_from_dict(self):
        """
        Te
        """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment.
        """
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear Down the test environment."""
        del self.storage
        del self.base_model

    def test_all(self):
        """
        Test the all() method.
        """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """
        Test the new() method.
        """
        self.storage.new(self.base_model)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.' + self.base_model.id, all_objects)
        self.assertEqual(
                all_objects['BaseModel.' + self.base_model.id],
                self.base_model)

    def test_save_reload(self):
        """Test the save() and reload() methods."""
        # Save the BaseModel Instance
        self.storage.new(self.base_model)
        self.storage.save()

        # Reload the data and check if BaseModel instance is present
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIn('BaseModel.' + self.base_model.id, all_objects)
        self.assertIsInstance(
                all_objects['BaseModel.' + self.base_model.id], BaseModel)

    def test_save_file_exists(self):
        """Test the save() method when the file exists."""
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_save_file_not_exists(self):
        """Test the save() method when the file does not exist."""
        os.remove(self.storage._FileStorage__file_path)
        self.assertFalse(os.path.exists(self.storage._FileStorage__file_path))
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))


if __name__ == '__main__':
    unittest.main()
