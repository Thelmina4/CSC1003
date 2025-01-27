#!/usr/bin/env python3

# cwd contains 2 files, a.txt, b.txt
# each has a seq of words, one/line

# s/o = every word in a, but NOT in b

import os
a, b = "a.txt", "b.txt"

with open(a, "r") as f, open(b, "r") as g:
   words_a, words_b = f.read().split(), g.read().split()
# print(words_a, words_b)

count = {}
i = 0
while i < len(words_a):
   word = words_a[i]
   if word not in count:
      count[word] = 0
   i += 1
# print(count)
j = 0
while j < len(words_b):
   word_b = words_b[j]
   if word_b in count:
      count[word_b] += 1
   j += 1

for key, value in count.items():
   if value == 0:
      print(key)
