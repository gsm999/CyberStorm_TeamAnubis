# Team: Anubis
# Names: Jalen Brown, Amani Cheatham, Abigail Folds, Emily Holis, 
# Gareth Maddox, Jayden Tarrance, Seonghoon Yi

import sys, datetime, hashlib

DEBUG = True

#getting epochtime
if DEBUG == False:
    epochtime = datetime.datetime.strptime(sys.stdin.read().strip('" \n'), "%Y %m %d %H %M %S").timestamp()
else:
    epochtime = datetime.datetime(2022, 10, 4, 23, 59, 59).timestamp()

#getting systemtime time
systime = datetime.datetime(2013, 5, 6, 7, 43, 25).timestamp()
if DEBUG == True: print(epochtime)

#calculating the time elasped
timeelp = systime - epochtime
div = (timeelp//60) * 60

#encoding the MD5 twice
result = hashlib.md5(str(int(div)).encode())
if DEBUG == True: print(result.hexdigest())

final = hashlib.md5(str(result.hexdigest()).encode())
if DEBUG == True: print(final.hexdigest())

end = ""
let = ['a','b','c','d','e','f']
num = [n for n in range(10)]
#finding the first two chars from left to right
for i in final.hexdigest():
    if i in let:
        if len(end) >= 2:
            break
        end = end + i

#finding the first two nums from right to left
for i in final.hexdigest()[::-1]:
    if i in str(num):
        if len(end) >= 4:
            break
        end = end + i

print(end)