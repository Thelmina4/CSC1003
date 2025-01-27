#!/usr/bin/env python3

# inside "start.txt" is a name of a file
# inside that file is the name of another file
# and so on until
# the last file has a word that doesn't match a file name
# print the word

import os

files = os.listdir(".")
content = "start.txt"

while content in files:
   with open(content, "r") as f:
      content = f.read().strip()

if content not in files:
   print(content)
