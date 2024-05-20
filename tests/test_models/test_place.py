#!/usr/bin/python3
"""Unit tests for the Place class"""

from models.place import Place
import unittest


class TestPlaceModel(unittest.TestCase):
    """Test suite for the Place class"""

    def test_instantiation(self):
        """Ensure the Place class is instantiated correctly"""
        p = Place()
        self.assertEqual(type(p.id), str)
        self.assertEqual(p.city_id, "")
        self.assertEqual(type(p.user_id), str)
        self.assertIsNotNone(p.created_at)
        self.assertIsNotNone(p.updated_at)

    def test_unique_id(self):
        """Check that each Place instance has a unique id"""
        p1 = Place()
        p2 = Place()
        p3 = Place()
        self.assertNotEqual(p1.id, p2.id)
        self.assertNotEqual(p2.id, p3.id)
        self.assertNotEqual(p1.id, p3.id)

    def test_save(self):
        """Verify that save() updates the updated_at attribute"""
        p = Place()
        initial_update_time = p.updated_at
        p.save()
        first_update_time = p.updated_at
        p.save()
        second_update_time = p.updated_at
        self.assertTrue(initial_update_time < first_update_time)
        self.assertTrue(first_update_time < second_update_time)
        self.assertTrue(initial_update_time < second_update_time)

    def test_str(self):
        """Check the string representation of the Place instance"""
        p = Place()
        p.name = "2BDRM Seaview"
        expected_string = "[{}] ({}) {}".format(p.__class__.__name__, p.id, p.__dict__)
        self.assertEqual(str(p), expected_string)

    def test_to_dict(self):
        """Test that to_dict() produces a correct dictionary representation"""
        p = Place()
        p.name = "2BDRM Seaview"
        p.save()
        place_dict = p.to_dict()
        self.assertEqual(len(place_dict), len(p.__dict__) + 1)
        self.assertEqual(place_dict["id"], p.id)
        self.assertEqual(place_dict["updated_at"], p.updated_at.isoformat())
        self.assertEqual(place_dict["created_at"], p.created_at.isoformat())
        self.assertEqual(place_dict["__class__"], p.__class__.__name__)
        self.assertEqual(place_dict["name"], p.name)

    def test_from_dict(self):
        """Ensure a Place instance can be created from a dictionary"""
        p = Place()
        p.name = "2BDRM Seaview"
        p.save()
        place_dict = p.to_dict()
        new_p = Place(**place_dict)
        self.assertEqual(p.id, new_p.id)
        self.assertEqual(p.name, new_p.name)
        self.assertEqual(p.created_at, new_p.created_at)
        self.assertEqual(p.updated_at, new_p.updated_at)

    def test_instantiation_with_args(self):
        """Ensure additional args on instantiation do not affect the instance"""
        p = Place()
        p2 = Place(p.id, p.created_at, p.updated_at)
        self.assertNotEqual(p.id, p2.id)
        self.assertTrue(p.created_at < p2.created_at)
        self.assertTrue(p.updated_at < p2.updated_at)


if __name__ == '__main__':
    unittest.main()
