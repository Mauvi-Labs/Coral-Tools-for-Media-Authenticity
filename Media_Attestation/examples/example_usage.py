from src.main import attest_media, verify_attestation

def main():
    username = "seriously alex"
    password = "securepassword"
    media_file = "example_media.jpg"

    try:
        # Create a dummy file for demonstration
        with open(media_file, 'wb') as f:
            f.write(b"This is a test media file.")

        # Attest media
        signature = attest_media(media_file, username, password)
        if signature:
            print(f"Media file attested. Signature: {signature}")

            # Verify attestation
            is_valid = verify_attestation(media_file, signature, username)
            print(f"Attestation is valid: {is_valid}")

            # Simulate tampering with the file
            with open(media_file, 'ab') as f:
                f.write(b'tampered')
            
            # Verify the tampered file
            is_valid = verify_attestation(media_file, signature, username)
            print(f"Tampered file attestation is valid: {is_valid}")
        else:
            print("Failed to attest media.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up the dummy file
        import os
        if os.path.exists(media_file):
            os.remove(media_file)

if __name__ == "__main__":
    main()
