#!/usr/bin/env python3

# s/i = seq of command lines that are txts
#      inside the txt are lines of ints

# s/o = the sum of each txt total

import sys
texts = sys.argv[1:]
total = 0

i = 0

while i < len(texts):
   files = texts[i]
   with open(files, "r") as f:
      # read the line, but there's a \n
      # so split it
      filei = f.read().split()
   j = 0
   while j < len(filei):
      number = filei[j]
      total += int(number)
      j += 1
   i += 1

print(total)
