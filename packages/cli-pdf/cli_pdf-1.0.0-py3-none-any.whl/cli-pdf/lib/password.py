import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def derive_key_from_password(password, salt=None, iterations=100000):
    if salt is None:
        salt = os.urandom(16)  # 16 bytes random salt
    
    key = hashlib.pbkdf2_hmac(
        'sha256',               # Hash algorithm
        password.encode(),       # Convert the password to bytes
        salt,                    # Use a random salt
        iterations,              # Number of iterations (high for security)
        dklen=32                 # AES-256 uses a 32-byte key
    )
    
    return key, salt

ENCRYPTION_MARKER = b'ENCRYPTED:'  # Kennzeichnung für verschlüsselte Dateien

def encrypt_file_with_password(input_file, output_file, password):
    # Read the input file to check if it's already encrypted
    with open(input_file, 'rb') as f:
        first_bytes = f.read(len(ENCRYPTION_MARKER))
        if first_bytes == ENCRYPTION_MARKER:
            print(f"Error: File '{input_file}' is already encrypted.")
            return

    # Derive the key from the password
    key, salt = derive_key_from_password(password)

    block_size = AES.block_size
    iv = get_random_bytes(block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read the input file
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Padding to make the length of the plaintext a multiple of the block size
    padding_length = block_size - len(plaintext) % block_size
    plaintext += bytes([padding_length]) * padding_length

    # Encrypt the file data
    ciphertext = cipher.encrypt(plaintext)

    # Write the encryption marker, salt, IV, and the ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(ENCRYPTION_MARKER + salt + iv + ciphertext)

    print(f"File '{input_file}' successfully encrypted to '{output_file}'.")



def decrypt_file_with_password(input_file, output_file, password):
    block_size = AES.block_size

    # Read the input file to check if it's encrypted
    with open(input_file, 'rb') as f:
        first_bytes = f.read(len(ENCRYPTION_MARKER))
        if first_bytes != ENCRYPTION_MARKER:
            print(f"Error: File '{input_file}' is not encrypted or is corrupt.")
            return

        salt = f.read(16)  # The next 16 bytes are the salt
        iv = f.read(block_size)  # The next block_size bytes are the IV
        ciphertext = f.read()

    # Derive the key from the password using the same salt
    key, _ = derive_key_from_password(password, salt)

    # Create AES cipher for decryption
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)

    # Remove padding
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]

    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"File '{input_file}' successfully decrypted to '{output_file}'.")

