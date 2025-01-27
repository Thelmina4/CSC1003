#!/usr/bin/env python3

# s/i = seq of lines, one / line
# terminated w "end"

# s/o = only the cities (s[:","])
# one per line

s = input()
while s != "end":
   i = 0
   while s[i] != ",":
      i += 1
   if s[i + 1:i + 3] == "WI":
      print(s[:i])
   s = input()
