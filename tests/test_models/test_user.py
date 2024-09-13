#!/usr/bin/python3
"""Unit tests for the User class"""

from models.user import User
import unittest


class TestUserModel(unittest.TestCase):
    """Test suite for the User class"""

    def test_instantiation(self):
        """Test for correct instantiation of User objects"""
        u = User()
        self.assertEqual(type(u.id), str)
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertIsNotNone(u.created_at)
        self.assertIsNotNone(u.updated_at)

    def test_unique_id(self):
        """Test to ensure each User instance has a unique ID"""
        u1 = User()
        u2 = User()
        u3 = User()
        self.assertNotEqual(u1.id, u2.id)
        self.assertNotEqual(u2.id, u3.id)
        self.assertNotEqual(u1.id, u3.id)

    def test_save(self):
        """Test that the updated_at attribute is updated correctly"""
        u = User()
        initial_update_time = u.updated_at
        u.save()
        first_update_time = u.updated_at
        u.save()
        second_update_time = u.updated_at
        self.assertTrue(initial_update_time < first_update_time)
        self.assertTrue(first_update_time < second_update_time)
        self.assertTrue(initial_update_time < second_update_time)

    def test_str(self):
        """Test the string representation of the User instance"""
        u = User()
        u.first_name = "Test"
        u.password = "1234"
        expected_string = "[{}] ({}) {}".format(u.__class__.__name__, u.id, u.__dict__)
        self.assertEqual(str(u), expected_string)

    def test_to_dict(self):
        """Test the to_dict method produces a correct dictionary representation"""
        u = User()
        u.name = "Test User"
        u.my_number = 42
        u.save()
        user_dict = u.to_dict()
        self.assertEqual(len(user_dict), len(u.__dict__) + 1)
        self.assertEqual(user_dict["id"], u.id)
        self.assertEqual(user_dict["updated_at"], u.updated_at.isoformat())
        self.assertEqual(user_dict["created_at"], u.created_at.isoformat())
        self.assertEqual(user_dict["__class__"], u.__class__.__name__)

    def test_from_dict(self):
        """Test creating a User instance from a dictionary"""
        u = User()
        u.first_name = "Test"
        u.password = "1234"
        u.save()
        user_dict = u.to_dict()
        new_u = User(**user_dict)
        self.assertEqual(u.id, new_u.id)
        self.assertEqual(u.first_name, new_u.first_name)
        self.assertEqual(u.password, new_u.password)
        self.assertEqual(u.created_at, new_u.created_at)
        self.assertEqual(u.updated_at, new_u.updated_at)

    def test_instantiation_with_args(self):
        """Test that passing args to the User constructor does not set attributes"""
        u = User()
        u2 = User(u.id, u.created_at, u.updated_at)
        self.assertNotEqual(u.id, u2.id)
        self.assertTrue(u.created_at < u2.created_at)
        self.assertTrue(u.updated_at < u2.updated_at)


if __name__ == '__main__':
    unittest.main()
