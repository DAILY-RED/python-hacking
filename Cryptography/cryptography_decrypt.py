from cryptography.fernet import Fernet
import cryptography_encrypt

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":

    key = cryptography_encrypt.load_key()
    filename = "test_file.txt"
    decrypt(filename, key)