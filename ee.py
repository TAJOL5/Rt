import os, sys
import DM
try:
    __import__("DM").main()
except Exception as e:
    exit(str(e))
