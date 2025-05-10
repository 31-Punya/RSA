"""
key_management.py
Handles RSA key generation, saving, and loading using the cryptography library.
"""
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

KEY_SIZE = 2048
PUBLIC_EXPONENT = 65537


def generate_key_pair():
    """Generate an RSA private/public key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=PUBLIC_EXPONENT,
        key_size=KEY_SIZE,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


def save_private_key(private_key, filepath, password=None):
    """Save a private key to a file, optionally encrypted with a password."""
    encryption = serialization.BestAvailableEncryption(password.encode()) if password else serialization.NoEncryption()
    with open(filepath, 'wb') as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryption
        ))


def save_public_key(public_key, filepath):
    """Save a public key to a file."""
    with open(filepath, 'wb') as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))


def load_private_key(filepath, password=None):
    """Load a private key from a file, optionally using a password."""
    with open(filepath, 'rb') as f:
        return serialization.load_pem_private_key(
            f.read(),
            password=password.encode() if password else None,
            backend=default_backend()
        )


def load_public_key(filepath):
    """Load a public key from a file."""
    with open(filepath, 'rb') as f:
        return serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )
