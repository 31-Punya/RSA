import unittest
from key_management import generate_key_pair
from encryption import encrypt_with_public_key, decrypt_with_private_key

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.private_key, self.public_key = generate_key_pair()
        self.message = b"Test message for encryption."

    def test_encrypt_decrypt(self):
        ciphertext = encrypt_with_public_key(self.public_key, self.message)
        plaintext = decrypt_with_private_key(self.private_key, ciphertext)
        self.assertEqual(plaintext, self.message)

if __name__ == '__main__':
    unittest.main()
