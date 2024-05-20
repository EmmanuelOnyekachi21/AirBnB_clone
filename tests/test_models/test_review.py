#!/usr/bin/python3
"""Unit tests for the Review class"""

from models.review import Review
import unittest


class TestReviewModel(unittest.TestCase):
    """Test suite for the Review class"""

    def test_instantiation(self):
        """Ensure proper instantiation of Review class"""
        r = Review()
        self.assertEqual(type(r.id), str)
        self.assertEqual(type(r.place_id), str)
        self.assertEqual(type(r.user_id), str)
        self.assertIsNotNone(r.created_at)
        self.assertIsNotNone(r.updated_at)

    def test_unique_id(self):
        """Verify that each Review instance has a unique id"""
        r1 = Review()
        r2 = Review()
        r3 = Review()
        self.assertNotEqual(r1.id, r2.id)
        self.assertNotEqual(r2.id, r3.id)
        self.assertNotEqual(r1.id, r3.id)

    def test_save(self):
        """Check that save() updates the updated_at attribute"""
        r = Review()
        initial_update_time = r.updated_at
        r.save()
        first_update_time = r.updated_at
        r.save()
        second_update_time = r.updated_at
        self.assertTrue(initial_update_time < first_update_time)
        self.assertTrue(first_update_time < second_update_time)
        self.assertTrue(initial_update_time < second_update_time)

    def test_str(self):
        """Ensure the string representation of the Review instance is correct"""
        r = Review()
        r.text = "My First Review"
        expected_string = "[{}] ({}) {}".format(r.__class__.__name__, r.id, r.__dict__)
        self.assertEqual(str(r), expected_string)

    def test_to_dict(self):
        """Test that to_dict() provides a correct dictionary representation"""
        r = Review()
        r.text = "My First Review"
        r.save()
        review_dict = r.to_dict()
        self.assertEqual(len(review_dict), len(r.__dict__) + 1)
        self.assertEqual(review_dict["id"], r.id)
        self.assertEqual(review_dict["updated_at"], r.updated_at.isoformat())
        self.assertEqual(review_dict["created_at"], r.created_at.isoformat())
        self.assertEqual(review_dict["__class__"], r.__class__.__name__)

    def test_from_dict(self):
        """Create a Review instance from a dictionary obtained from to_dict()"""
        r = Review()
        r.text = "Great experience"
        r.save()
        review_dict = r.to_dict()
        new_r = Review(**review_dict)
        self.assertEqual(r.id, new_r.id)
        self.assertEqual(r.text, new_r.text)
        self.assertEqual(str(r), str(new_r))
        self.assertEqual(r.created_at, new_r.created_at)
        self.assertEqual(r.updated_at, new_r.updated_at)

    def test_instantiation_with_args(self):
        """Ensure additional args on instantiation do not affect the instance"""
        r = Review()
        r2 = Review(r.id, r.created_at, r.updated_at)
        self.assertNotEqual(r.id, r2.id)
        self.assertTrue(r.created_at < r2.created_at)
        self.assertTrue(r.updated_at < r2.updated_at)


if __name__ == '__main__':
    unittest.main()
