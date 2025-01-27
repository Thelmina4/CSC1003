#!/usr/bin/env python3

# s/i = command-line arguments consist of a seq of ints

# s/o = sum of the ints

import sys

args = sys.argv[1:]

total = 0

i = 0
while i < len(args):
   total += int(args[i])
   i += 1

print(total)
