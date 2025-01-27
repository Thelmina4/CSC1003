#!/usr/bin/env python3

# no input from s/i or command line

# output = all the non empty .py files
#          that have the she bang in the first line
#          or that end in .py

# operating system
import os

files = os.listdir(".")

i = 0
while i < len(files):
   if files[i][len(files[i]) - 3:] == ".py":
      with open(files[i]) as f:
         content = f.read()
         if 0 < len(content):
            print(files[i])
   else:
      with open(files[i]) as f:
         content = f.read()
         shebang = "#!/usr/bin/env python3\n"
         if content[:len(shebang)] == shebang:
            print(files[i])
   i += 1
