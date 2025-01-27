#!/usr/bin/env python3

# cwd contains 2 files, a.txt & b.txt

# s/o = only the words that are in BOTH lists

import os

a, b = "a.txt", "b.txt"
# print(a, b)

with open(a, "r") as f, open(b, "r") as g:
   words_a = f.read().split()
   words_b = g.read().split()
# print(words_a, words_b)
dict = {}

i = 0
while i < len(words_a):
   word = words_a[i]
   if word not in dict:
      dict[word] = True
   i += 1

i = 0
while i < len(words_b):
   word_b = words_b[i]
   if word_b in dict:
      print(word_b)
   i += 1
