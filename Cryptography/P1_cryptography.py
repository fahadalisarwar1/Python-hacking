# Encryption is the process of encoding an information in such a way that only authorized parties can access it.
from cryptography.fernet import Fernet 

if __name__ == "__main__":

    key = Fernet.generate_key()
    print("Key: ", key)

    msg = "This is a secret message"
    msg_bin = msg.encode()
    f = Fernet(key)
    encrypted_msg = f.encrypt(msg_bin)
    print("Encrypted message: ", encrypted_msg)

    decrypted = f.decrypt(encrypted_msg)
    print(decrypted.decode())