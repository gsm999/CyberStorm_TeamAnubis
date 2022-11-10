#Team Anubis#
#Jayden Tarrance, Jalen Brown, Amani Cheatham, Abigail Folds, Emily Hollis, Gareth Maddox, Seonghoon Yi

import sys, getopt

sent = bytearray(6)
sent[0] = 0x0
sent[1] = 0xff
sent[2] = 0x0
sent[3] = 0x0
sent[4] = 0xff
sent[5] = 0x0

def main(argv):
    mode = ''
    method = ''
    offset = 0
    interval = 1
    wrapper = ''
    hidden = ''
    try:
        opts, args = getopt.getopt(argv,"srbBo:i:w:h:",["oval=","ival=","wfile=","hfile="])
    except getopt.GetoptError:
        print("Usage:")
        print("python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<file> [-h<file>]")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-s':
            method = 's'
        elif opt == '-r':
            method = 'r'
        elif opt == '-b':
            mode = 'b'
        elif opt == '-B':
            mode = 'B'
        elif opt in ("-o", "--oval"):
            offset = int(arg)
        elif opt in ("-i", "--ival"):
            interval = int(arg)
        elif opt in ("-w", "--wfile"):
            wrapper = str(arg)
        elif opt in ("-h", "--hfile"):
            hidden = str(arg)

    if mode == 'b':
        bit(method, offset, interval, wrapper, hidden)
    elif mode == 'B':
        byte(method, offset, interval, wrapper, hidden)
    else:
        print("Usage:")
        print("python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<file> [-h<file>]")
        print("-s store")
        print("-r retrieve")
        print("-b bit mode")
        print("-B byte mode")
        print("-o<val> set offset to <val> (default is 0)")
        print("-i<val> set interval to <val> (default is 1)")
        print("-w<val> set wrapper file to <val>")
        print("-h<val> set hidden file to <val>")

def bit(method, offset, interval, wrapper, hidden):
    wrapper = open(wrapper, 'rb').read()
    wrapper = bytearray(wrapper)
    
    if method == 's':
        hidden = open(hidden, 'rb').read()
        hidden = bytearray(hidden)
        for i in range(len(hidden)):
            for j in range(8):
                wrapper[offset] = wrapper[offset] & 0b11111110
                wrapper[offset] = wrapper[offset] | ((hidden[i] & 0b10000000) >> 7)
                hidden[i] = (hidden[i] <<  1) & 0xff 
                offset += interval

        #stores the sentinel values
        for i in range(len(sent)):
            for j in range(8):
                wrapper[offset] = wrapper[offset] & 0b11111110
                wrapper[offset] = wrapper[offset] | ((sent[i] & 0b10000000) >> 7)
                sent[i] = (sent[i] << 1) & 0xff 
                offset += interval
                
            
        sys.stdout.buffer.write(wrapper)
            
    if method == 'r':
        hidden = bytearray()
        s = bytearray()
        while offset < len(wrapper)-10:
            
            b = 0x0
            for j in range(8):
                b = b | (wrapper[offset] & 0b00000001)
                if j < 7:
                    b = (b << 1) & 0xff
                    offset += interval
        
            offset += interval
            #checks if b is first sentinel and then checks the next 5
            if b == sent[0]:
                s.append(b)
                tempoff = offset
                for h in range(5):
                    temp = 0x0
                    for g in range(8):
                        temp = temp | (wrapper[tempoff] & 0b00000001)
                        if g < 7:
                            temp = (temp << 1) & 0xff
                            tempoff += interval
                    tempoff += interval
                    s.append(temp)

            #checks if sentinel has been reached
            if s == sent:
                break
            else:
                s = bytearray()

            hidden.append(b)
           
        sys.stdout.buffer.write(hidden)

def byte(method, offset, interval, wrapper, hidden):
    wrapper = open(wrapper, 'rb').read()
    wrapper = bytearray(wrapper)
    
    if method == 's':
        hidden = open(hidden, 'rb').read()
        hidden = bytearray(hidden)
        for i in hidden:
            wrapper[offset] = i
            offset += interval

        #stores the sentinel values
        for i in sent:
            wrapper[offset] = i
            offset+=interval
        
        sys.stdout.buffer.write(wrapper)

    if method == 'r':
        hidden = bytearray()
        while offset < len(wrapper):
            ##check for sentinel
            if wrapper[offset] == sent[0]:
                if wrapper[offset+interval] == sent[1]:
                    if wrapper[offset+(interval*2)] == sent[2]:
                        if wrapper[offset+(interval*3)] == sent[3]:
                            if wrapper[offset+(interval*4)] == sent[4]:
                                if wrapper[offset+(interval*5)] == sent[5]:
                                    break #if sentinel
            hidden.append(wrapper[offset])
            offset += interval
                
        sys.stdout.buffer.write(hidden)
        

if __name__ == '__main__':
    main(sys.argv[1:])