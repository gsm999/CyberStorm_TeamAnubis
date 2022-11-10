
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




