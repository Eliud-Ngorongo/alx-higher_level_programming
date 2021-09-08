#!/usr/bin/python3
def uppercase(str):
   """Print a string in uppercase"""
   for c in str:
     if c >= 'a' and c <= 'z':
        c = chr(ord(c) - 32)
     print("{:s}".format(c), end='')
   print('')