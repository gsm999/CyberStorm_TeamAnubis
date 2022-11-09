from ftplib import FTP
DEBUG = False

IP = "138.47.134.55"
PORT = 8008
USER = "osiris"
PASSWORD = "encryptiongods"
FOLDER = "/.secretstorage/.folder2/.howaboutonemore"
USE_PASSIVE = True

ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)
ftp.cwd(FOLDER)
temp = []
ftp.dir(temp.append)

ftp.quit()

#change between 7 & 10 for 7bit method or 10bit method
method = 10

def method10(temp):
	message = ""
	bin = ""
	files = []
	split = 7
	
	for f in temp:
		if DEBUG == True:
			print(f)
		files.append(f[0:10])

	for n in files:
		for p in n:
			if p == "-":
				bin+= "0"
			else:
				bin+= "1"
	
	#splits bin every 7 bits
	chunks = [bin[i:i+split] for i in range(0, len(bin), split)]
	
	for i in chunks:
		message+=chr(int(i, 2))

	print(message)

def method7(temp):
	message = ""
	bin = ""
	files = []
	split = 7

	for f in temp:
		if DEBUG == True:
			print(f)
		##ignores file with anything in the first 3 bits
		if f[0] != "-" or f[1] != "-" or f[2] != "-":
			continue
		files.append(f[3:10])

	for n in files:
		for p in n:
			if p == "-":
				bin += "0"
			else:
				bin += "1"
	
	#splits bin every 7 bits
	chunks = [bin[i:i+split] for i in range(0, len(bin), split)]

	for i in chunks:
		message+=chr((int(i, 2)))

	print(message)
	
if method == 7:
	method7(temp)
elif method == 10:
	method10(temp)


