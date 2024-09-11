"""
Tests
"""


import unittests
from models.base_model import BaseModel



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
        initial_update = self.model.updated_at
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
