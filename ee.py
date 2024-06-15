import os, sys
try:
    __import__("fo9").main()
except Exception as e:
    exit(str(e))