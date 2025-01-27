#!/usr/bin/env python3

# s/i = command line args of file names
#       in the files are ints,
#       but there are spaces eg 2 3

# s/o = the sum of all ints

import sys

total = 0

files = sys.argv[1:]

i = 0
while i < len(files):
   with open(files[i], "r") as f:
      filei = f.read().split()
   # print(filei)
   j = 0
   while j < len(filei):
      number = filei[j]
      total += int(number)
      j += 1
   i += 1

print(total)
