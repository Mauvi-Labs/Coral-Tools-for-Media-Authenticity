# Coral: Tools for Media Authenticity

Updating....Coral combines vision models with attestation techniques and other cryptographic tools to offer solutions for media verification and authentication. 

# Media Attestation Technique No. 01

The media attestation technique in this project provides a tool for cryptographic signatures, particularly designed for use in social media platforms. It allows users to sign media files and verify the authenticity of signed media.

## Features

- RSA key pair generation and management
- Media file signing using RSA private keys
- Signature verification using RSA public keys
- User-friendly high-level functions for easy integration
- Error handling for file operations and key management
- Secure password handling

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Mauvi-Labs/Coral-Tools-for-Media-Authenticity.git
   cd Coral-Tools-for-Media-Authenticity/Media_Attestation
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Here's a basic example of how to use the media attestation tool:

```python
from src.main import attest_media, verify_attestation

username = "seriously alex"
password = "securepassword"
media_file = "example_media.jpg"

# Attest media
signature = attest_media(media_file, username, password)
if signature:
    print(f"Media file attested. Signature: {signature}")

    # Verify attestation
    is_valid = verify_attestation(media_file, signature, username)
    print(f"Attestation is valid: {is_valid}")
```

## Project Structure

- `src/attestation/`: Contains the core attestation functionality
- `src/utils/`: Contains utility functions like key management
- `src/main.py`: Provides high-level functions for easy integration
- `tests/`: Contains unit tests for the project
- `examples/`: Contains example usage scripts

## Running Tests

To run the unit tests:

```
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

