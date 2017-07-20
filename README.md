This is a little utility to encrypt and decrypt a file based on a passphrase. It's not the most secure thing in the world, but perhaps it makes up for it in convenience. It's a little python app with two entrypoints that can be built into two executables (small enough to be stored with your encrypted files!). Throw it all on a thumb drive and not have to worry about anything but the passphrase.

If I ever want to do anything more with it, I'll DRY it out (duh), maybe make a class or two, non-happy-path tests, and a proper command line client with only one entry path and more configuration.

setup:
```sh
PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install -v 3.4.3
pyenv virtualenv 3.4.3 file_encrypt
pyenv activate file_encrypt
pip install -r requirements-dev.txt
```

tests:
```sh
py.test
```

build:
```sh
pyinstaller --onefile decrypt.py
pyinstaller --onefile encrypt.py
```

encrypt: `python encrypt.py` or after building it... `./dist/encrypt`

decrypt: `python decrypt.py` or after building it... `./dist/decrypt`
