"""
validation.py
Validates that a public key matches a private key by signing and verifying a test message.
"""
from signing import sign_with_private_key, verify_signature
import os

def validate_key_pair(private_key, public_key) -> bool:
    """Validate that the public key matches the private key by signing and verifying a test message."""
    test_message = os.urandom(32)
    signature = sign_with_private_key(private_key, test_message)
    return verify_signature(public_key, test_message, signature)
