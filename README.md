
# Summary of codes for Cyberstorm

Every code is assumed to run on Linux Mint Enviroment.

# [Vigenere] 




## general info
- people in charge for Cyberstorm: Abigail Folds, Seonghoon Yi
- Code Author: Abigail Folds
- file name: CSC442_Ven.py

## example

After putting the below command,

```bash
yourid@servername:~$ python3 CSC442_Ven.py -d "This is my key" 
```

start to typing strings you want to encrypt.
```bash
hello <----- this is my input
tcvpm <----- this is the output
HELLO <------ this is my input
TCVPM <------ this is my output
```

There is another way to use with '>' & '<'.


for example, if you want to encrypt a sentence and save it as a file named 'ciphertext.txt', you can do it by typing as below.
```bash
yourid@servername:~$ python3 CSC442_Ven.py -e "This is my key" > ciphertext.txt
```

Vice versa, If you want to decrypt the encrypted sentence with the same key, you can do that as below.

```bash
yourid@servername:~$ python3 CSC442_Ven.py -d "This is my key" < ciphertext.txt
```

then the reuslt will be printed on the prompt.


# [Timelock]

## general info
- people in charge for Cyberstorm: Abigail Folds, Seonghoon Yi
- Code Author: Abigail Folds
- file name: timelock.py


## example

You can do this program by commandline, which would look like this:

```bash
yourid@servername:~$ echo "1999 12 31 23 59 59" | python timelock.py
```

This will work perfectly fine, But as you have to manually change the system time manually anyway, I would suggest turning DEBUG on and manually filling in the epoch and system time.

This would look like this.

```bash
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
```

The printed result will have the 4 digit code.