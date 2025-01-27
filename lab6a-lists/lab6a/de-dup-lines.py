#!/usr/bin/env python3

# s/i = seq of lines, terminated w "end"

# s/o = only the 1st occurance of the line

seen = []

s = input()
while s != "end":
   i = 0
   while i < len(seen) and seen[i] != s:
      i += 1
   if i == len(seen):
      print(s)
      seen.append(s)
   s = input()
