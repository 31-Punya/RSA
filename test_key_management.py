import unittest
from key_management import generate_key_pair, save_private_key, save_public_key, load_private_key, load_public_key
import os

class TestKeyManagement(unittest.TestCase):
    def setUp(self):
        self.private_path = 'tests/test_private.pem'
        self.public_path = 'tests/test_public.pem'
        self.password = 'testpass'
        # Clean up before each test
        for f in [self.private_path, self.public_path]:
            if os.path.exists(f):
                os.remove(f)

    def tearDown(self):
        for f in [self.private_path, self.public_path]:
            if os.path.exists(f):
                os.remove(f)

    def test_generate_and_save_load_keys(self):
        private_key, public_key = generate_key_pair()
        save_private_key(private_key, self.private_path, self.password)
        save_public_key(public_key, self.public_path)
        loaded_private = load_private_key(self.private_path, self.password)
        loaded_public = load_public_key(self.public_path)
        self.assertIsNotNone(loaded_private)
        self.assertIsNotNone(loaded_public)

if __name__ == '__main__':
    unittest.main()
