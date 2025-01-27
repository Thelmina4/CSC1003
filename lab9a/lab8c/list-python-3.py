#!/usr/bin/env python3

# no input from s/i or command line

# output = all the non empty .py files
#          that have the shebang in the first line
#          or that end in .py

# operating system
import os

files = os.listdir(".")
sbg = "#!/usr/bin/env python3\n"
p = ".py"
# ls = len(shebang)

i = 0
while i < len(files):
   file = files[i]
   with open(file, "r") as f:
      lines = f.readlines()
      lf = len(file) - 3
      lenl = len(lines)
      if lenl != 0:
         lio = lines[0]
         if(lf == p or lio == sbg):
            print(file)
   i += 1
