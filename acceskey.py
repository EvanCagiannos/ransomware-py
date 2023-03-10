# import the Fernet module from the cryptography library
from cryptography.fernet import Fernet

# generate a new 
key = Fernet.generate_key()

# print the key
print(key)

# write the key to a file named "thekey.key" in binary mode
with open("thekey.key", "wb") as thekey:
    thekey.write(key)  
cat thekey.key

# ------- DECRYPTION --------

files = []

# loop through the files in the current directory
for file in os.listdir():
    if file == "thekey.key" == or "privatekey.key" or == "decrypt.py"
        continue 
    if os.path.isfile(file):
        files.append(file)

# print the list of files to be encrypted
print(files)

with open("thekey.key", "rb") as key: 
        secretkey = key.read()
        
        # read the contents of the file
        contents = thefile.read()
        # encrypt the contents using the generated key
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        # open the file in binary write mode
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
