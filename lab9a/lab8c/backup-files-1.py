#!/usr/bin/env python3

# create a back up file :
#       filename.txt -> filename.txt.bak
#      do nothing if the last 4 == ".bak"

# do to all files in dir

import os
files = os.listdir(".")
bak = ".bak"
i = 0
while i < len(files):
   if os.path.isfile(files[i]):
      # print(files[i])
      file_name = files[i]
      if file_name[len(file_name) - 4:] != bak:
         # print(file_name)
         bak_file = file_name + bak
         with open(file_name, "r") as f, open(bak_file, "w") as g:
            content = f.read()
            g.write(content)
            # use: rm *."bak" to delete all after
   i += 1
