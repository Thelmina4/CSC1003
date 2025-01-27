#!/usr/bin/env python3

# s/i = seq o words, one per line

# s/o = eg snap: dog
#       only the FIRST TIME there is a snap
#       and nothing if there is no snap

import sys

words = sys.stdin.read().split()
seen = ""
snap = {}
# print(type(words))
i = 0
while i < len(words):
   word = words[i]
   if word not in snap:
      snap[word] = True
   elif word in snap:
      seen = word
      i = len(words)
   i += 1

if 0 < len(seen):
   print("snap:", seen)
