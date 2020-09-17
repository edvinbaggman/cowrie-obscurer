#!/usr/bin/python3

import urllib.request

print("Retrieving a sanitized OUI file from \"https://linuxnet.ca/\".")
try:
	urllib.request.urlretrieve("https://linuxnet.ca/ieee/oui.txt", filename="oui.txt")
except Exception:
	print("Could not retrieve the OUI file. Exiting.")
	exit()
print("Printing list of OUIs.")
ouiarray = []
ouifile = open("oui.txt", 'r')
while (True):
	line = ouifile.readline()
	if not line:
		break
	if line[0] == '\n':
		continue
	print(line)