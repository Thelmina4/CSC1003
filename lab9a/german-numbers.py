#!/usr/bin/env python3

# s/i = seq of line, each is a no in english

# s/o = translation of thos numbers to german

import sys

eng = sys.stdin.read().split()
english = "one two three four five six seven eight nine ten".split()
german = "eins zwei drei vier funf sechs sieben acht neun zehn".split()

dict = {}
i = 0
while i < len(english):
   dict[english[i]] = german[i]
   i += 1

# print(dict)
j = 0
while j < len(eng):
   word = eng[j]
   if word in dict:
      print(dict[word])
   j += 1
