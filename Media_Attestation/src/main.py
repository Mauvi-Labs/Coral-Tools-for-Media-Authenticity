from .attestation.rsa_signing import sign_file, verify_file_signature
from .utils.key_management import generate_or_load_keys

def attest_media(file_path, user_id, password):
    try:
        private_key, _ = generate_or_load_keys(user_id, password)
        return sign_file(file_path, private_key)
    except Exception as e:
        print(f"Error attesting media: {e}")
        return None

def verify_attestation(file_path, signature, user_id):
    try:
        _, public_key = generate_or_load_keys(user_id, "dummy")  # Password not needed for public key
        return verify_file_signature(file_path, signature, public_key)
    except Exception as e:
        print(f"Error verifying attestation: {e}")
        return False
