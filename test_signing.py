import unittest
from key_management import generate_key_pair
from signing import sign_with_private_key, verify_signature

class TestSigning(unittest.TestCase):
    def setUp(self):
        self.private_key, self.public_key = generate_key_pair()
        self.data = b"Test data for signing."

    def test_sign_and_verify(self):
        signature = sign_with_private_key(self.private_key, self.data)
        valid = verify_signature(self.public_key, self.data, signature)
        self.assertTrue(valid)

    def test_invalid_signature(self):
        signature = sign_with_private_key(self.private_key, self.data)
        invalid = verify_signature(self.public_key, b"tampered", signature)
        self.assertFalse(invalid)

if __name__ == '__main__':
    unittest.main()
