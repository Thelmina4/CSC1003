#!/usr/bin/env python3

# list all files in the current and all sub directories

import os

cwd = os.listdir("./")

listdirs = [cwd]
i = 0
# cwd is a list of strings
while i < len(listdirs):
   curr_dir = listdirs[i]
   print(curr_dir)
   j = 0
   while j < len(curr_dir):
      if os.path.isfile(curr_dir[j]):
         print(curr_dir[j])
      else:
         
         listdirs.append(curr_dir[j])
         curr_dir[j] = os.listdir("./")
      j += 1
      #  with open(curr_dir[i]) as f:
      # all_files = f.readlines()
      # print(all_files)
      # if os.path.isfile(all_files[i]):
      #    print(all_files[i])
      # j = 0
      # while j < len(all_files):
      #   if os.path.isdir(all_files[j]):
      #      listdirs.append("./" + all_files[j] + "/")
      #   j += 1
   i += 1
print(cwd)
