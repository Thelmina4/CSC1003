#!/usr/bin/env python3

# s/i = command-line arguments consist of a seq of words
# e.g. python3 SOMETHING.py dog cat mouse

# s/o = those, one per line

import sys

args = sys.argv[1:]

i = 0
while i < len(args):
   print(args[i])
   i += 1
