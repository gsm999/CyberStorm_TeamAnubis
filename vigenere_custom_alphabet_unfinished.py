import sys

e_d = sys.argv[1]
key = sys.argv[2]

key.replace('"',"")
key.replace(" ", "")

key = key.upper()

alph = {}
revalph = {}

count = 0
for i in range(65,91):
    alph.update({chr(i): count})
    revalph.update({count : chr(i)})
    count +=1

while(1):
    try:
        e_string = input()
    except(EOFError):
        pass
    cyphered = [""] * len(e_string)
    cypherstring = ""
    if e_d == "-e":
        for j in range(0,len(key)):
            for i in range(j,len(e_string)):
                token = e_string[i]
                val = ord(token)
                if val == 8:
                    cyphered[i-1] = ""
                elif (val >= 65 and val< 91) or (val >= 97 and val< 123):
                    if e_string[i].isupper(): cyphtoken = revalph[(alph[token] + alph[key[j]])%26]
                    else: cyphtoken = (revalph[(alph[token.upper()] + alph[key[j]])%26]).lower()
                    cyphered[i] = cyphtoken
                else:
                    cyphered[i] = token
    else:
        for j in range(0,len(key)):
            for i in range(j,len(e_string)):
                token = e_string[i]
                val = ord(token)
                if val == 8:
                    cyphered[i-1] = ""
                elif (val >= 65 and val< 91) or (val >= 97 and val< 123):
                    if e_string[i].isupper(): cyphtoken = revalph[(alph[token] + alph[key[j]])%26]
                    else: cyphtoken = (revalph[(alph[token.upper()] - alph[key[j]])%26]).lower()
                    cyphered[i] = cyphtoken
                else:
                    cyphered[i] = token
    for i in cyphered:
        cypherstring += i
    print(cypherstring)