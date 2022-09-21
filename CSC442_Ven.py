# Abigail Folds
# 9/15/2022
# Description: This program implements the Vegenere cipher, Takes the arguments of "-e" to encrypt
#   a message, or "-d" to decrpt a message. Also takes in an argument of the key, which is made into lower case letters.


import sys, getopt

#Pre-Declared variables
enckey = []
inword = []

#This functions take in plaintext and a key, and encrypts the plaintext
def Encr(enkey, inword):
    r = 0
    outword = []
    for i in inword:
        #Make sure that the current letter is between "a-z" or "A-Z", everything else is skipped.
        if (ord(i) >= 65 and ord(i) < 91):
            #Capital Letters
            outword.append(chr(((ord(i)-65)+(ord(enkey[r%(len(enkey))])-97))%26+65))
            r += 1
        elif (ord(i)>=97 and ord(i) < 123):
            #Lower Case Letters
            outword.append(chr(((ord(i)-97)+(ord(enkey[r%(len(enkey))])-97))%26+97))
            r += 1
        else:
            #anything that is not a letter, is not touched by the encrypt
            outword.append(i)

    print("".join(outword))

#This functions takes in a encrpted message and decrepts it to plaintext, based on a key.
def Decr(enkey, inword):
    r = 0
    outword = []

    for i in inword:
        #Make sure that the current letter is between "a-z" or "A-Z", everything else is skipped.
        if (ord(i) >= 65 and ord(i) < 91):
            #Capital Letters
            outword.append(chr(((26+ord(i)-65)-(ord(enkey[r%(len(enkey))])-97))%26+65))
            r += 1
        elif (ord(i)>=97 and ord(i) < 123):
            #Lower Case Letters
            outword.append(chr(((26+ord(i)-97)-(ord(enkey[r%(len(enkey))])-97))%26+97))
            r += 1
        else:
            #anything that is not a letter, is not encrypted
            outword.append(i)

    print("".join(outword))
#sees if the arguments are correct, if not display error
try:
    opts, args = getopt.getopt(sys.argv[1:], "e:d:", "inkey=")
except getopt.GetoptError:
    print("CSC442_Ven.py -e <key> -d <key>")

#Checks to see if -e or -d was used, running the correct code after
for opt, arg in opts:
    if opt in ("-e", "--inkey"):
        enckey = [*arg.lower().replace(" ","")]
        while True:
            try:
                inword = [*input()]
                Encr(enckey, inword)
            except KeyboardInterrupt:
                exit()
    elif opt in ("-d", "--inkey"):
        enckey = [*arg.lower().replace(" ","")]
        while True:
            try:
                inword = [*input()]
                Decr(enckey, inword)
            except:
                exit()











