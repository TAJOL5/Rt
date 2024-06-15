import os, platform, time, sys
G1 = '\x1b[1;92m\x1b[38;5;50m'
G2 = '\x1b[1;92m\x1b[38;5;212m'
G3 = '\x1b[1;92m\x1b[38;5;208m'
os.system('clear')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print(f'{G1}- {G3}Hi Your 32 bit Go Tols .')
 time.sleep(4)
 import GOLDEN64
elif bit == '32bit':
 print(f'{G1}- {G2}Hi Your 32 bit Go Tols .')
 time.sleep(4)
 import GOLDEN
