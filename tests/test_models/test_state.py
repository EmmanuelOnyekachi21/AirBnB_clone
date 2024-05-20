#!/usr/bin/python3
"""Unit tests for the State class"""

from models.state import State
import unittest


class TestStateModel(unittest.TestCase):
    """Test suite for the State class"""

    def test_instantiation(self):
        """Test correct instantiation of State objects"""
        s = State()
        self.assertEqual(type(s.id), str)
        self.assertEqual(s.name, "")
        self.assertIsNotNone(s.created_at)
        self.assertIsNotNone(s.updated_at)

    def test_unique_id(self):
        """Test to ensure each State instance has a unique ID"""
        s1 = State()
        s2 = State()
        s3 = State()
        self.assertNotEqual(s1.id, s2.id)
        self.assertNotEqual(s2.id, s3.id)
        self.assertNotEqual(s1.id, s3.id)

    def test_save(self):
        """Test that the updated_at attribute is updated correctly"""
        s = State()
        initial_update_time = s.updated_at
        s.save()
        first_update_time = s.updated_at
        s.save()
        second_update_time = s.updated_at
        self.assertTrue(initial_update_time < first_update_time)
        self.assertTrue(first_update_time < second_update_time)
        self.assertTrue(initial_update_time < second_update_time)

    def test_str(self):
        """Test the string representation of the State instance"""
        s = State()
        s.name = "Oyo State"
        expected_string = "[{}] ({}) {}".format(s.__class__.__name__, s.id, s.__dict__)
        self.assertEqual(str(s), expected_string)

    def test_to_dict(self):
        """Test the to_dict method produces a correct dictionary representation"""
        s = State()
        s.name = "Oyo State"
        s.save()
        state_dict = s.to_dict()
        self.assertEqual(len(state_dict), len(s.__dict__) + 1)
        self.assertEqual(state_dict["id"], s.id)
        self.assertEqual(state_dict["updated_at"], s.updated_at.isoformat())
        self.assertEqual(state_dict["created_at"], s.created_at.isoformat())
        self.assertEqual(state_dict["__class__"], s.__class__.__name__)

    def test_from_dict(self):
        """Test creating a State instance from a dictionary"""
        s = State()
        s.name = "Oyo State"
        s.save()
        state_dict = s.to_dict()
        new_s = State(**state_dict)
        self.assertEqual(s.id, new_s.id)
        self.assertEqual(s.name, new_s.name)
        self.assertTrue(s.created_at == new_s.created_at)
        self.assertTrue(s.updated_at == new_s.updated_at)

    def test_instantiation_with_args(self):
        """Test that passing args to the State constructor does not set attributes"""
        s = State()
        s2 = State(s.id, s.created_at, s.updated_at)
        self.assertNotEqual(s.id, s2.id)
        self.assertTrue(s.created_at < s2.created_at)
        self.assertTrue(s.updated_at < s2.updated_at)


if __name__ == '__main__':
    unittest.main()
