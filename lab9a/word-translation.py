#!/usr/bin/env python3

# cwd contains translation.txt.
# inside the file is a seq of lines w eng german translations

# s/i = from sys.stdin a seq of words

# s/o = their translations

import sys
import os

file = "translation.txt"
with open(file, "r") as f:
   t = f.readlines()
dict = {}
# print(t)

i = 0
while i < len(t):
   line = t[i].strip().split()
   # print(line)
   dict[line[0]] = line[1]
   i += 1

words = sys.stdin.read().split()
j = 0
while j < len(words):
   word = words[j]
   if word in dict:
      print(dict[word])
   j += 1

# print(translations)
