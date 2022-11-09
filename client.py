#### CLIENT.py
#### TEAM anubis
#### 10/14/22

import socket
import sys
import time

IP = "138.47.102.167"
PORT = 1337    

DEBUG = False
         
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP/IP NETWORK
s.connect((IP, PORT))


binary = ''
timeCheck = (0.1 + 0.025) / 2


print("From server: ", end= "\n")
data = s.recv(4096).decode("utf-8")
# Print each line until at 'EOF'
while (data.rstrip("\n") != "EOF"):
    # Decode data from bytes into string
        sys.stdout.write(data)
        sys.stdout.flush()
        startTime = time.time()
        data = s.recv(4096).decode("utf-8") 
        # Check the time it took to recieve the data 
        # Greater than 0.0625 add 1, otherwise 0 
        endTime = time.time() - startTime
        if round(time.time() - startTime, 3) > timeCheck:
            binary += '1'
        else: 
            binary += '0'
    
s.close()

covert = ''
i=0

print()
# Convert from string to hex to text
while (i < len(binary)-7):
     # process one byte at a time
    b = binary[i:i + 8]
    # convert it to ASCII
    n = int(b, 2)
    
    try:
        covert += chr(n)

    except TypeError:
        covert += "?"
    # stop at the string "EOF"
    i += 8


print(f'Covert: {covert}')