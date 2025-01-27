#!/usr/bin/env python3

# s/i = seq of words, terminated by end
# s/o = only the words where the letters are in alphabetical order
# try linear search
s = input()
while s != "end":
   # loop keeps going until
   # s[i - 1] <= s[i]
   i = 1
   while i < len(s) and s[i - 1] <= s[i]:
      i += 1

   if len(s) == i:
      print(s)

   s = input()
