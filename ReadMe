# RSA-Based Python Application

## Overview
This project is a Python application that demonstrates secure data transmission and digital signatures using RSA encryption. It provides a command-line interface (CLI) for generating RSA key pairs, encrypting and decrypting data, signing and verifying data, and validating key pairs. The project is modular, with each cryptographic operation implemented in a separate module for clarity and maintainability.

## Features
- **RSA Key Generation**: Create secure public/private key pairs (2048 bits or higher).
- **Key Storage and Loading**: Save and load keys in PEM format, with optional password protection for private keys.
- **Data Encryption/Decryption**: Encrypt data with a public key and decrypt with the corresponding private key.
- **Digital Signing/Verification**: Sign data with a private key and verify signatures with the public key.
- **Key Pair Validation**: Confirm that a public key matches a private key by signing and verifying a test message.
- **Command-Line Interface**: Perform all operations via a user-friendly CLI.
- **Unit Tests**: Comprehensive tests for all modules.

## Project Structure
```
key_management.py        # Key generation, saving, loading
encryption.py            # Encryption and decryption logic
signing.py               # Signing and signature verification
validation.py            # Key pair validation
cli.py                   # Command-line interface
requirements_and_features.md # Project requirements and features
ReadMe                   # This documentation

tests/                   # Unit tests for all modules
```

## Requirements
- Python 3.7 or higher
- [cryptography](https://pypi.org/project/cryptography/) (for RSA operations)
- argparse (standard library, for CLI)

## Setup Instructions
1. **Clone the repository** (if applicable):
   ```sh
   git clone <your-repo-url>
   cd rsa-project
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Linux/Mac
   ```
3. **Install dependencies:**
   ```sh
   pip install cryptography argparse
   ```

## Usage
All operations are performed using the `cli.py` script. Activate your virtual environment before running commands.

### 1. Generate RSA Key Pair
Generate a new RSA key pair and save them to files. Optionally, protect the private key with a password.
```sh
python cli.py generate-keys --private PRIVATE_KEY_PATH --public PUBLIC_KEY_PATH [--password PASSWORD]
```

### 2. Encrypt Data
Encrypt a file using a public key.
```sh
python cli.py encrypt --public PUBLIC_KEY_PATH --infile INPUT_FILE --outfile OUTPUT_FILE
```

### 3. Decrypt Data
Decrypt a file using a private key. If the private key is password-protected, provide the password.
```sh
python cli.py decrypt --private PRIVATE_KEY_PATH --infile INPUT_FILE --outfile OUTPUT_FILE [--password PASSWORD]
```

### 4. Sign Data
Sign a file using a private key. The signature is saved to a separate file.
```sh
python cli.py sign --private PRIVATE_KEY_PATH --infile INPUT_FILE --outfile SIGNATURE_FILE [--password PASSWORD]
```

### 5. Verify Signature
Verify a signature using the public key.
```sh
python cli.py verify --public PUBLIC_KEY_PATH --infile INPUT_FILE --signature SIGNATURE_FILE
```

### 6. Validate Key Pair
Check if a public key matches a private key.
```sh
python cli.py validate --private PRIVATE_KEY_PATH --public PUBLIC_KEY_PATH [--password PASSWORD]
```

### 7. CLI Help
For a full list of commands and options:
```sh
python cli.py --help
```

## Example Workflow
1. Generate keys:
   ```sh
   python cli.py generate-keys --private my_private.pem --public my_public.pem --password mypass
   ```
2. Encrypt a file:
   ```sh
   python cli.py encrypt --public my_public.pem --infile message.txt --outfile message.enc
   ```
3. Decrypt the file:
   ```sh
   python cli.py decrypt --private my_private.pem --infile message.enc --outfile message_decrypted.txt --password mypass
   ```
4. Sign a file:
   ```sh
   python cli.py sign --private my_private.pem --infile message.txt --outfile message.sig --password mypass
   ```
5. Verify the signature:
   ```sh
   python cli.py verify --public my_public.pem --infile message.txt --signature message.sig
   ```
6. Validate key pair:
   ```sh
   python cli.py validate --private my_private.pem --public my_public.pem --password mypass
   ```

## Security Notes
- **Keep your private key secure.** Never share it. Only distribute the public key.
- **Use strong passwords** for private key encryption.
- **Use strong key sizes** (2048 bits or higher).
- **Handle files securely**: Do not leave sensitive files unprotected on disk.
- **Exception Handling**: The CLI and modules handle errors gracefully and will print helpful messages for common issues.

## Testing
Unit tests are provided for all modules. To run all tests:
```sh
venv\Scripts\python -m unittest discover tests
```
All tests should pass if the environment is set up correctly.

## Troubleshooting
- If you see `ModuleNotFoundError`, ensure your virtual environment is activated and dependencies are installed.
- For permission errors, check file paths and access rights.
- For cryptography errors, ensure you are using a supported Python version and the latest `cryptography` library.

## Contributing
Feel free to fork this project and submit pull requests. Please include tests for any new features or bug fixes.

## License
This project is provided for educational purposes. Adapt and use as needed for your own projects.

## References
- [cryptography documentation](https://cryptography.io/en/latest/)
- [Python argparse documentation](https://docs.python.org/3/library/argparse.html)
