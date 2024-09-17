import unittest
import os
import tempfile
from src.utils.key_management import save_private_key, load_private_key, save_public_key, load_public_key, generate_or_load_keys

class TestKeyManagement(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.username = "testuser"
        self.password = "testpassword"

    def tearDown(self):
        for file in os.listdir(self.test_dir):
            os.unlink(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_generate_and_load_keys(self):
        private_key, public_key = generate_or_load_keys(self.username, self.password)
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)

        # Test loading existing keys
        loaded_private_key, loaded_public_key = generate_or_load_keys(self.username, self.password)
        self.assertEqual(private_key.private_numbers(), loaded_private_key.private_numbers())
        self.assertEqual(public_key.public_numbers(), loaded_public_key.public_numbers())

    def test_invalid_password(self):
        generate_or_load_keys(self.username, self.password)
        with self.assertRaises(ValueError):
            generate_or_load_keys(self.username, "wrongpassword")

if __name__ == '__main__':
    unittest.main()