import sys

inputfile = open(sys.argv[1])
message = inputfile.read()
message = message[0:-1]
length = 0
outmessage = ''

# Check if the bitstream uses 7 or 8 bit ASCII encoding
if ((len(message))%7 == 0):
	length = 7
elif ((len(message))%8 == 0):
	length = 8
else:
    print("Invalid number of bits!")
    sys.exit()
    
# Take the entire bitstream and iterate(step) by the encoding bit-size
# Each iteration captures a new 7or8 bits. (No need to split & then join the string)
for i in range(0,len(message)-1,length):
    temp = ''
    # After "seperating" the binary, concatenate each bit
    for j in range(length):
        temp += message[i+j]
        # So we don't print the same line "length" amount of times, after concatenating a number
        continue
        #sys.stdout.write(outmessage+'\n') 
    
    # Convert the binary into an integer with base of 2
    # Then, convert into a string       
    char = chr(int(temp, base=2))
    #sys.stdout.write(outmessage+'\n') 
    
    # If you backspace, return everything up until its pressed
    # Backspace is registered, but not included in the output
    if char == '\b':
        outmessage = outmessage[0:-1]
    else: outmessage += char
    
sys.stdout.write(outmessage)