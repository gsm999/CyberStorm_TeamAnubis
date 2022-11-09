### Team anubis ###
###     XOR     ### 
###  10/28/22   ###

import sys

KEY_FILE = "key"

# Open the file with key
# r -read, b-binary
with open(KEY_FILE, "rb") as key:
    data = key.read()
    
# Read the file from command line(stdin) as bytes
encrypted = bytearray(sys.stdin.buffer.read())
key = bytearray(data)

# Check equality of byte length
if len(encrypted) != len(key):
	print("size mismatch", end='')

# Iterate over encrypted text and XOR with the key
# Write the result to command line(stdout) as text
decryptTxt = []
for i in range(len(encrypted)):
	decryptTxt.append(encrypted[i] ^ key[i])
 
sys.stdout.buffer.write(bytes(decryptTxt))
       
