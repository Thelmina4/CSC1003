#!/usr/bin/env python3

# s/i = string with spaces in it
# s/o = the string w no spaces

s = input()
t = ""
i = 0
while i < len(s):
   if s[i] != " ":
      t = t + s[i]
   i += 1

print(t)
