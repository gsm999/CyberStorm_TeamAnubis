Usage:
	python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]
	-s store
	-r retrieve
	-b bit mode
	-B byte mode
	-o<val> set offset to <val> (default is 0)
	-i<val> set interval to <val> (default is 1)
	-w<val> set wrapper file to <val>
	-h<val> set hidden file to <val>
	
e.g. 
	python Steg.py -s -B -o1024 -i256 -wimage.jpg -hsecret.jpg > new.jpg 
This combines secret.jpg and image.jpg and stores it into new.jpg

	python Steg.py -r -B -o1024 -i256 -wnew.jpg > extracted.jpg
This retrieves secret.jpg from new.jpg and stores it in extracted.jpg
