import unittest
from key_management import generate_key_pair
from validation import validate_key_pair

class TestValidation(unittest.TestCase):
    def setUp(self):
        self.private_key, self.public_key = generate_key_pair()
        other_private, self.other_public = generate_key_pair()

    def test_valid_key_pair(self):
        self.assertTrue(validate_key_pair(self.private_key, self.public_key))

    def test_invalid_key_pair(self):
        self.assertFalse(validate_key_pair(self.private_key, self.other_public))

if __name__ == '__main__':
    unittest.main()
