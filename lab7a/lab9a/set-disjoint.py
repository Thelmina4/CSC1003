#!/usr/bin/env python3

# cwd: current working directory
# contains 2 files, a.txt & b.txt
# each containing seq of words, 1/line

# s/o = either "disjoint" or "intersecting"

import os

a, b = "a.txt", "b.txt"

with open(a, "r") as f, open(b, "r") as g:
   words_a, words_b = f.read().split(), g.read().split()
# print(words_a, words_b)

dict = {}

i = 0
while i < len(words_a):
   word_a = words_a[i]
   if word_a not in dict:
      dict[word_a] = 0
   i += 1
# print(dict)
total = 0
i = 0
while i < len(words_b):
   word_b = words_b[i]
   if word_b in dict:
      total += 1
   i += 1

if total == 0:
   print("disjoint")
else:
   print("intersecting")
