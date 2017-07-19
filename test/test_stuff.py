import os

from encrypt import run as encrypter
from decrypt import run as decrypter


def test_integration():
    original_string = 'type, count, whatever\ntest, 2, skittles\nfunzies, 12, shenanigans\n'
    expected_decrypted_file_contents = 'type, count, whatever\ntest, 2, skittles\nfunzies, 12, shenanigans\n'
    passphrase = passphrase_two = 'these pretzels are making me thirsty.'

    input_file_path = 'test/sample.csv'
    encrypted_file_path = 'test/encrypted.dat'
    decrypted_file_path = 'test/decrypted.csv'

    with open(input_file_path, "wb") as f:
        f.write(str.encode(original_string))

    encrypter(passphrase, passphrase_two, input_file_path, encrypted_file_path)
    decrypter(passphrase, encrypted_file_path, decrypted_file_path)

    with open(decrypted_file_path, "r") as f:
        decrypted_file_contents = f.read()

    assert decrypted_file_contents == expected_decrypted_file_contents

    os.remove(input_file_path)
    os.remove(encrypted_file_path)
    os.remove(decrypted_file_path)
