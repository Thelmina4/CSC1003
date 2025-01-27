#!/usr/bin/env python3

# standard in = seq od words, one/line

# s/o = only the words that occur once

import sys

s = sys.stdin.readlines()

count = {}

i = 0
while i < len(s):
   word = s[i].rstrip()
   if word not in count:
      count[word] = 0
   else:
      count[word] += 1
   i += 1

# print(count)

j = 0
while j < len(s):
   word = s[j].rstrip()
   if count[word] == 0:
      print(word)
   j += 1
