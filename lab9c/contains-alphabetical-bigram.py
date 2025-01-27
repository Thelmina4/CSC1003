#!/usr/bin/env python3

# s/i = seq of words, one/line

import sys

words = sys.stdin.read().split()
# print(words)
dict = {}
i = 0
while i < len(words):
   word = words[i]
   j = 1
   while j < len(word):
      char1 = word[j - 1]
      next = word[j]
      # print(char1 + next)
      # print((ord(char1) + 1) + next
      if ord(char1) + 1 == ord(next):
         print(word)
         j = len(word)
      j += 1
   i += 1
