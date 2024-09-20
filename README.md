# Coral: Tools for Media Authenticity

Updating....Coral combines vision models with attestation techniques and other cryptographic tools to offer solutions for media verification and authentication. 

# Media Attestation Technique No. 01

The first media attestation technique in this project provides a tool for cryptographic signatures, particularly designed for use in social media platforms. It allows users to sign media files and verify the authenticity of signed media.

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

# Media Attestation Technique No. 02

The second technique provides an **Ethereum Attestation Service (EAS)**-based **media attestation** technique for verifying the authenticity of media, specifically images and videos. It is designed to serve social media platforms and generative AI video platforms where users can attest media, verify its authenticity, and display a custom badge for verified content.

## Features

- **Media Upload**: Users can upload media (images or videos) and generate a unique hash for attestation.
- **Ethereum Attestation Service (EAS) Integration**: The media hash is attested and verified using the EAS protocol.
- **Badge System**: Verified media is displayed with an "OG 🖌️" badge to indicate authenticity.
- **Dark Mode Support**: The interface is styled for dark mode.

### Key Components

- **`contracts/MediaAttestation.sol`**: A smart contract that interacts with the Ethereum Attestation Service (EAS) to handle the attestation and verification process for media hashes.
  
- **`EAS_config.js`**: Provides a helper function to configure the EAS SDK and connect it with an Ethereum wallets.

- **`UI/components/MediaUploader.js`**: Allows users to upload media (images or videos) and calculates a SHA-256 hash, which is then used for attestation.

- **`UI/components/AttestationBadge.js`**: Displays a custom "OG 🖌️" badge for verified media or leaves it empty if the media is not verified.

- **`UI/components/MediaCard.js`**: Displays the uploaded media in a card-like format, along with the verification badge.

- **`UI/pages/index.js`**: The main Next.js page where media upload, attestation, and verification take place. It integrates the `MediaUploader`, `MediaCard`, and handles the attestation flow using the EAS SDK.

---

## Installation

### Prerequisites

- **Node.js** (v14.x or above)
- **Metamask** or any Ethereum-compatible wallet
- **Hardhat** (for deploying the smart contract)
- **Next.js** (for the frontend)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Media_Attestation_Technique2.git
   cd Media_Attestation_Technique2
   
2. **Install dependencies**:
   
npm install

3. **Deploy the smart contract using hardhat**
   
npx hardhat run scripts/deploy.js --network <your-network>

4. **Start Next.js**
   
npm run dev

5. **Connect an ethereum wallet**
   Make sure to connect an ethrreum wallet to the correct Ethereum network (e.g., Rinkeby, Mainnet, etc.).

---

## Contributions

This project is **open-source** and welcomes contributions from the community. Feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License.

