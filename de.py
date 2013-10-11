#!/usr/bin/python
import sys
import base64


for inputtext in sys.stdin:
	print repr(inputtext)
	print len(inputtext)
	inputtext = inputtext[:-1]
	print repr(inputtext)
	print len(inputtext)
	print inputtext[0:1]
	print inputtext[1:2]
	print inputtext[2:3]
	print inputtext[3:4]
	print inputtext[4:5]
	print inputtext[5:6]
	print inputtext[1:2]
