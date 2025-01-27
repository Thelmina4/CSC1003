#!/usr/bin/env python3

# s/i = string
# s/o = reversed string

s = input()
t = ""
i = 0

while i < len(s):
   t = s[i] + t
   i += 1

print(t)
