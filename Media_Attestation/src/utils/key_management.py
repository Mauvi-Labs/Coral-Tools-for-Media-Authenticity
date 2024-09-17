import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from .rsa_signing import generate_key_pair

def save_private_key(private_key, filename, password):
    encrypted_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )
    try:
        with open(filename, 'wb') as f:
            f.write(encrypted_private_key)
    except IOError as e:
        print(f"Error saving private key: {e}")

def load_private_key(filename, password):
    try:
        with open(filename, 'rb') as f:
            encrypted_private_key = f.read()
        private_key = serialization.load_pem_private_key(
            encrypted_private_key,
            password=password.encode(),
            backend=default_backend()
        )
        return private_key
    except IOError as e:
        print(f"Error loading private key: {e}")
    except ValueError as e:
        print(f"Invalid password or corrupted key file: {e}")

def save_public_key(public_key, filename):
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    try:
        with open(filename, 'wb') as f:
            f.write(public_key_bytes)
    except IOError as e:
        print(f"Error saving public key: {e}")

def load_public_key(filename):
    try:
        with open(filename, 'rb') as f:
            public_key_bytes = f.read()
        public_key = serialization.load_pem_public_key(
            public_key_bytes,
            backend=default_backend()
        )
        return public_key
    except IOError as e:
        print(f"Error loading public key: {e}")
    except ValueError as e:
        print(f"Corrupted public key file: {e}")

def generate_or_load_keys(username, password):
    private_key_file = f"{username}_private_key.pem"
    public_key_file = f"{username}_public_key.pem"

    if os.path.exists(private_key_file) and os.path.exists(public_key_file):
        private_key = load_private_key(private_key_file, password)
        public_key = load_public_key(public_key_file)
    else:
        private_key, public_key = generate_key_pair()
        save_private_key(private_key, private_key_file, password)
        save_public_key(public_key, public_key_file)

    return private_key, public_key