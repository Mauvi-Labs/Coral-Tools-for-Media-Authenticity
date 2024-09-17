from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature
import base64

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_file(file_path, private_key):
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        signature = private_key.sign(
            file_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode()
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"Error signing file: {e}")

def verify_file_signature(file_path, signature, public_key):
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        public_key.verify(
            base64.b64decode(signature),
            file_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    except IOError as e:
        print(f"Error reading file: {e}")
        return False
    except Exception as e:
        print(f"Error verifying signature: {e}")
        return False