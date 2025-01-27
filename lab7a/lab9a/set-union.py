#!/usr/bin/env python3

# the CWD cnotains 2 files; a.txt, b.txt
# each file contains a seq of words, one per line

# s/o = every word that occurs in either file
#       NO DUPLICATES ALLOWED

import os
a = "a.txt"
b = "b.txt"
with open(a, "r") as f, open(b, "r") as g:
   words = f.read().split() + g.read().split()

# print(words_a, "\n", words_b)
# print(words)
dict = {}
i = 0
while i < len(words):
   word = words[i]
   if word not in dict:
      # print(word, type(word))
      dict[word] = True
      print(word)
   i += 1
