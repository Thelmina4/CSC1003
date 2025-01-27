#!/usr/bin/env python3

# same as the last, not sure what the difference is
# make back up fils for all the files in the dir

import os

# os, list of all the files in current working dir
files = os.listdir(".")

bak = ".bak"

i = 0
while i < len(files):
   if os.path.isfile(files[i]):
      file = files[i]
      bak_file = file + bak
      if file[len(file) - 4:] != bak and bak_file not in files:
         with open(file, "r") as f, open(bak_file, "w") as g:
            content = f.read()
            g.write(content)
   i += 1
