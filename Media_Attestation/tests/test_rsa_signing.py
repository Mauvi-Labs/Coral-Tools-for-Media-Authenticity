import unittest
import tempfile
import os
from src.attestation.rsa_signing import generate_key_pair, sign_file, verify_file_signature

class TestRSASigning(unittest.TestCase):
    def setUp(self):
        self.private_key, self.public_key = generate_key_pair()
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        with open(self.test_file.name, 'wb') as f:
            f.write(b"Test content")

    def tearDown(self):
        os.unlink(self.test_file.name)

    def test_sign_and_verify(self):
        signature = sign_file(self.test_file.name, self.private_key)
        self.assertIsNotNone(signature)
        self.assertTrue(verify_file_signature(self.test_file.name, signature, self.public_key))

    def test_invalid_signature(self):
        signature = sign_file(self.test_file.name, self.private_key)
        with open(self.test_file.name, 'ab') as f:
            f.write(b"Tampered content")
        self.assertFalse(verify_file_signature(self.test_file.name, signature, self.public_key))

    def test_nonexistent_file(self):
        signature = sign_file("nonexistent_file.txt", self.private_key)
        self.assertIsNone(signature)
        self.assertFalse(verify_file_signature("nonexistent_file.txt", "invalid_signature", self.public_key))

if __name__ == '__main__':
    unittest.main()
