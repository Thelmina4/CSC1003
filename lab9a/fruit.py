#!/usr/bin/env python3

# s/i = seq of words, one per line

# s/o = only the words which are fruit

import sys
words = sys.stdin.read().split()
#print(words)

f = "apple pear orange banana cherry".split()
dict = {}

i = 0
while i < len(f):
   dict[f[i]] = True
   i += 1

# print(dict)
j = 0
while j < len(words):
   word = words[j]
   # print(word)
   if word in dict:
      print(word)
   j += 1
