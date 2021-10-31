#!/usr/bin/env -S python3 -B

import shell_codes
from shell_codes import *

print(
"""\x1b[36m———————————————————————————————————————————————————————————————
\x1b[31m   _________.__           .__  .__          __________        
  /   _____/|  |__   ____ |  | |  | ___.__. \______   \___.__.
  \_____  \ |  |  \_/ __ \|  | |  |<   |  |  |     ___<   |  |
  /        \|   Y  \  ___/|  |_|  |_\___  |  |    |    \___  |
 /_______  /|___|  /\___  >____/____/ ____|  |____|    / ____|
         \/      \/     \/          \/                 \/     
\x1b[36m———————————————————————————————————————————————————————————————\033[0m""")

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
