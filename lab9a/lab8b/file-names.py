#!/usr/bin/env python3

# s/i = file names eg file-names.py/filenames.py

# s/o = only the file name,
# which seems to be the last after /

import sys

line = sys.stdin.readline()

while 0 < len(line):
   line = line.strip()
   file = line.split("/")
   print(file[len(file) - 1])
   line = sys.stdin.readline()
