# import the Fernet module from the cryptography library
from cryptography.fernet import Fernet

# generate a new key
key = Fernet.generate_key()

# print the key
print(key)

# write the key to a file named "thekey.key" in binary mode
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
