from cryptography.fernet import Fernet


def encrypt_file(filename, key):
    f = Fernet(key)
    encrypted = b''
    with open(filename, "rb") as file:
        data = file.read()

        encrypted = f.encrypt(data)
    with open(filename, "wb") as file:
        file.write(encrypted)

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

def write_key(key):
    with open("key.key", "wb") as file:
        file.write(key)

def load_key():
    return open("key.key").read()

    
if __name__ == "__main__":
    # key = Fernet.generate_key()
    # write_key(key)
    key = load_key()

    filename = "test_file.txt"
    # encrypt_file(filename, key)
    decrypt(filename, key)

