import os
import base64
import getpass

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


# http://incolumitas.com/2014/10/19/using-the-python-cryptography-module-with-custom-passwords/
def get_key(password):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    return base64.urlsafe_b64encode(digest.finalize())

def encrypt(password, content):
    f = Fernet(get_key(password))
    return f.encrypt(bytes(content))

def decrypt(password, content):
    f = Fernet(get_key(password))
    return f.decrypt(bytes(content))

def run(password, encrypted_file_path, decrypted_file_path):
    password_bytes = str.encode(password)
    if not os.path.exists(encrypted_file_path):
        raise BaseException('That file does not exist.')
    if os.path.exists(decrypted_file_path):
        # if the file is already there, add another `.csv` because why not
        decrypted_file_path += '.csv'
    with open(encrypted_file_path, "rb") as f:
        encrypted_content = f.read()
    decrypted_content = decrypt(password_bytes, encrypted_content)
    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_content)

if __name__ == '__main__':
    print("DECRYPTING...")
    # get inputs
    password = getpass.getpass(prompt='Passphrase: ')
    encrypted_file_path = input("encrypted file path (e.g. `encrypted.dat`): ") or 'encrypted.dat'
    decrypted_file_path = input("decrypted file path (e.g. `unencrypted.csv`): ") or 'unencrypted.csv'

    run(password, encrypted_file_path, decrypted_file_path)
