#!/usr/bin/env python3

# s/i = 1. seq of nos, terminated in "end"
#       2. one command line arg
# e.g python3 grep-lines.py Mary

# s/o = only the lines that contain the word in the command line

import sys

grep = sys.argv[1]
m = len(grep)

a = []
s = input()
while s != "end":
   # if it contains the grep append
   i = 0
   while i < len(s):
      if s[i:i + m] == grep:
         a.append(s)
         print(s)
         i = len(s)
      i += 1
   s = input()
# print(a)
