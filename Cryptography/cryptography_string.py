# from cryptography.fernet import Fernet

# if __name__ == "__main__":

#     key = Fernet.generate_key()
#     print("Key: ", key)

#     msg = "This is a secret message"
#     msg_bin = msg.encode()
#     f = Fernet(key)
#     encrypted_msg = f.encrypt(msg_bin)
#     print("Encrypted message: ", encrypted_msg)

#     decrypted = f.decrypt(encrypted_msg)
#     print(decrypted.decode())



from cryptography.fernet import Fernet

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

if __name__ == "__main__":
    key = Fernet.generate_key()
    #print("Key:", key.decode())

    msg = input("Enter the message to be encrypted: ")
    encrypted_msg = encrypt_message(msg, key)
    print("Encrypted message:", encrypted_msg.decode())

    decrypted = decrypt_message(encrypted_msg, key)
    #print("Decrypted message:", decrypted)






