#!/usr/bin/env python3

# s/i = command line args
#       the first is the file to write to argv[1]
#       rest is the lines to input to the file [2:]

# output = the lines into a file

import sys

file_name = sys.argv[1]
lines = sys.argv[2:]

# print(lines)
with open(file_name, "w") as f:
   i = 0
   while i < len(lines):
      f.write(lines[i] + "\n")
      i += 1
