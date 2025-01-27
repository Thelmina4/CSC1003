#!/usr/bin/env python3

# input = must have empty .py file in dir for testing
#        must put .txt file in dir - testing

# output = only the NON empty .py

# import operating system
import os

files = os.listdir(".")

i = 0
while i < len(files):
   if files[i][len(files[i]) - 3:] == ".py":
      # print(files[i])
      file = files[i]
      with open(file, "r") as f:
         content = f.read().rstrip()
         # print(content[])
         if 0 < len(content):
            print(file)
   i += 1
