from cryptography.fernet import Fernet


def encrypt_file(filename, key):
    f = Fernet(key)
    encrypted = b''
    with open(filename, "rb") as file:
        data = file.read()

        encrypted = f.encrypt(data)
    with open(filename, "wb") as file:
        file.write(encrypted)

def write_key(key):
    with open("key.key", "wb") as file:
        file.write(key)

def load_key():
    return open("key.key").read()

if __name__ == "__main__":

    key = Fernet.generate_key()
    write_key(key)
    
    filename = "test_file.txt"
    encrypt_file(filename, key)