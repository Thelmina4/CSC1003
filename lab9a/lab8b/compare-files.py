#!/usr/bin/env python3

# like einstein compares files,
# we do the same here
# eg python3 compare-files.py a.txt b.txt

# output = nothing if the files are identical
#          not identical? output the
#          line and pos


import sys

text1 = sys.argv[1]
text2 = sys.argv[2]

with open(text1, "r") as f1, open(text2, "r") as f2:
   lines1 = f1.readlines()
   lines2 = f2.readlines()

# print("lines1:", lines1)
#print("lines2:", lines2)

# run through the lines in the 2 cases
i = 0
while i < len(lines1) and i < len(lines2):
   line1 = lines1[i]
   line2 = lines2[i]
   j = 0
   # run through the char in each line
   while j < len(line1) and j < len(line2):
      char1 = line1[j]
      char2 = line2[j]
      # not equal char
      if char1 != char2:
         print(i, j)
      j += 1
   # came to end of line, but one is longer
   if len(line1) < len(line2):
      diff = len(line2) - len(line1)
      print(i, line2[len(line2) - diff])
   elif len(line2) < len(line2):
      diff = len(line1) - len(line2)
      print(i, line1[len(line1) - diff])
   i += 1

# he'll have a test case where there is an extra line in one text

if i < len(lines1) and i == len(lines2):
   print(i, 0)
if i < len(lines2) and i == len(lines1):
   print(i, 0)
