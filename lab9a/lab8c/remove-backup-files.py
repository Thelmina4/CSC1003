#!/usr/bin/env python3

# remove backup files
# os.unlink(file_name)

# only if it is a file and not a dir
# remove * backups from current working dir

import os

files = os.listdir(".")

i = 0
while i < len(files):
   file = files[i]
   if os.path.isfile(file):
      if file[len(file) - 4:] == ".bak":
         os.unlink(files[i])
   i += 1
