"""
cli.py
Command-line interface for RSA operations.
"""
import argparse
from key_management import generate_key_pair, save_private_key, save_public_key, load_private_key, load_public_key
from encryption import encrypt_with_public_key, decrypt_with_private_key
from signing import sign_with_private_key, verify_signature
from validation import validate_key_pair
import sys


def main():
    parser = argparse.ArgumentParser(description="RSA-Based Python Application CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Key generation
    gen_parser = subparsers.add_parser("generate-keys", help="Generate RSA key pair")
    gen_parser.add_argument("--private", required=True, help="Path to save private key")
    gen_parser.add_argument("--public", required=True, help="Path to save public key")
    gen_parser.add_argument("--password", help="Password to encrypt private key (optional)")

    # Encrypt
    enc_parser = subparsers.add_parser("encrypt", help="Encrypt data with public key")
    enc_parser.add_argument("--public", required=True, help="Path to public key")
    enc_parser.add_argument("--infile", required=True, help="Input file to encrypt")
    enc_parser.add_argument("--outfile", required=True, help="Output file for ciphertext")

    # Decrypt
    dec_parser = subparsers.add_parser("decrypt", help="Decrypt data with private key")
    dec_parser.add_argument("--private", required=True, help="Path to private key")
    dec_parser.add_argument("--infile", required=True, help="Input file (ciphertext)")
    dec_parser.add_argument("--outfile", required=True, help="Output file for plaintext")
    dec_parser.add_argument("--password", help="Password for private key (optional)")

    # Sign
    sign_parser = subparsers.add_parser("sign", help="Sign data with private key")
    sign_parser.add_argument("--private", required=True, help="Path to private key")
    sign_parser.add_argument("--infile", required=True, help="Input file to sign")
    sign_parser.add_argument("--outfile", required=True, help="Output file for signature")
    sign_parser.add_argument("--password", help="Password for private key (optional)")

    # Verify
    verify_parser = subparsers.add_parser("verify", help="Verify signature with public key")
    verify_parser.add_argument("--public", required=True, help="Path to public key")
    verify_parser.add_argument("--infile", required=True, help="Input file (original data)")
    verify_parser.add_argument("--signature", required=True, help="Signature file")

    # Validate key pair
    val_parser = subparsers.add_parser("validate", help="Validate public/private key pair")
    val_parser.add_argument("--private", required=True, help="Path to private key")
    val_parser.add_argument("--public", required=True, help="Path to public key")
    val_parser.add_argument("--password", help="Password for private key (optional)")

    args = parser.parse_args()

    if args.command == "generate-keys":
        private_key, public_key = generate_key_pair()
        save_private_key(private_key, args.private, args.password)
        save_public_key(public_key, args.public)
        print("Keys generated and saved.")

    elif args.command == "encrypt":
        public_key = load_public_key(args.public)
        with open(args.infile, "rb") as f:
            plaintext = f.read()
        ciphertext = encrypt_with_public_key(public_key, plaintext)
        with open(args.outfile, "wb") as f:
            f.write(ciphertext)
        print("Data encrypted.")

    elif args.command == "decrypt":
        private_key = load_private_key(args.private, args.password)
        with open(args.infile, "rb") as f:
            ciphertext = f.read()
        plaintext = decrypt_with_private_key(private_key, ciphertext)
        with open(args.outfile, "wb") as f:
            f.write(plaintext)
        print("Data decrypted.")

    elif args.command == "sign":
        private_key = load_private_key(args.private, args.password)
        with open(args.infile, "rb") as f:
            data = f.read()
        signature = sign_with_private_key(private_key, data)
        with open(args.outfile, "wb") as f:
            f.write(signature)
        print("Data signed.")

    elif args.command == "verify":
        public_key = load_public_key(args.public)
        with open(args.infile, "rb") as f:
            data = f.read()
        with open(args.signature, "rb") as f:
            signature = f.read()
        if verify_signature(public_key, data, signature):
            print("Signature is valid.")
        else:
            print("Signature is invalid.")
            sys.exit(1)

    elif args.command == "validate":
        private_key = load_private_key(args.private, args.password)
        public_key = load_public_key(args.public)
        if validate_key_pair(private_key, public_key):
            print("Key pair is valid.")
        else:
            print("Key pair is invalid.")
            sys.exit(1)

if __name__ == "__main__":
    main()
