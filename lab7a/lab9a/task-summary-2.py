#!/usr/bin/env python3

# stdin = seq of lines
# eg user-1/word-translation.py.correct

# the user is correct as per the final upload for that .py

# s/o = the user and the no of times that they are correct

# make a dict for the user,
# where the value is a dict of .py and correct/incorrect

import sys

user_dict = {}

for line in sys.stdin:
   # print(line)
   user_code = line.strip().split("/")
   user = user_code[0]
   code = 
