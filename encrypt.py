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

def run(password, password_two, input_file_path, output_file_path):
    if password != password_two:
        raise "your passwords didn't match. try again."
    password_bytes = str.encode(password)
    # verify input
    if not os.path.exists(input_file_path):
        raise "that file doesn't exist!"
    if os.path.exists(output_file_path):
        # if the file is already there, add another `.dat` because why not
        output_file_path += '.dat'
    # read in, encrypt, write out
    with open(input_file_path, "rb") as f:
        content = f.read()
    encrypted_content = encrypt(password_bytes, content)
    with open(output_file_path, "wb") as f:
        f.write(encrypted_content)

if __name__ == '__main__':
    print("ENCRYPTING...")
    # get inputs
    password = getpass.getpass(prompt='Passphrase: ')
    password_two = getpass.getpass(prompt='Passphrase again: ')
    input_file_path = input("unencrypted file path (e.g. `unencrypted.csv`): ") or 'unencrypted.csv'
    output_file_path = input("encrypted file path (e.g. `encrypted.dat`): ") or 'encrypted.dat'

    run(password, password_two, input_file_path, output_file_path)
