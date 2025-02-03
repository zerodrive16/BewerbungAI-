import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from WebApplication.Text_Preprocessing.hashing import *


class TestHashingFunctions(unittest.TestCase):

    def test_hashing(self):
        """Test if hashing returns a non-empty string."""
        user_info = "test_password"
        hashed_info = hashing(user_info)

        self.assertIsInstance(hashed_info, str)
        self.assertNotEqual(user_info, hashed_info)
        self.assertTrue(len(hashed_info) > 0)

    def test_verifyHash_correct(self):
        """Test if verifyHash returns True for correct input."""
        user_info = "test_password"
        hashed_info = hashing(user_info)

        self.assertTrue(verifyHash(user_info, hashed_info))

    def test_verifyHash_incorrect(self):
        """Test if verifyHash returns False for incorrect input."""
        user_info = "test_password"
        hashed_info = hashing(user_info)

        self.assertFalse(verifyHash("wrong_password", hashed_info))


if __name__ == "__main__":
    unittest.main()
