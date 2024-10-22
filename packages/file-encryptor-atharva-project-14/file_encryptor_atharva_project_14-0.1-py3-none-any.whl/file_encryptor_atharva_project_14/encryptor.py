from cryptography.fernet import Fernet

class FileEncryptor:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_file(self, input_file_path, output_file_path):
        """Encrypts a file and writes the encrypted content to a new file."""
        with open(input_file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.cipher.encrypt(file_data)

        with open(output_file_path, 'wb') as file:
            file.write(encrypted_data)
        print(f"File '{input_file_path}' encrypted successfully!")

    def decrypt_file(self, encrypted_file_path, output_file_path):
        """Decrypts a file and writes the decrypted content to a new file."""
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self.cipher.decrypt(encrypted_data)

        with open(output_file_path, 'wb') as file:
            file.write(decrypted_data)
        print(f"File '{encrypted_file_path}' decrypted successfully!")

    def get_key(self):
        """Returns the encryption key."""
        return self.key
