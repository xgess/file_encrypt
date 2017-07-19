This is messy AF but the idea is a little utility to encrypt and decrypt a file based on a passphrase. It's not the most secure thing in the world, but perhaps it makes up for it in convenience? There are two entry points and each will guide you through finding the file and entering a passphrase that you can remember.

If I ever want to do anything more with it, I'll DRY it out (duh), maybe make a class or two, non-happy-path tests, and a proper command line client with one entry path. Maybe an easier-to-distribute executable.
But you know, sometimes when you want to encrypt and decrypt a file, you just want the basics.

encrypt:
```sh
python encrypt.py
```

decrypt:
```sh
python decrypt.py
```

tests:
```sh
py.test
```
