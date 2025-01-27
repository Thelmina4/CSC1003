#!/usr/bin/env python3

# s/i = string
# s/o = the string reversed w one s[i] per line

s = input()

i = 0
while i < len(s):
   print(s[len(s) - i - 1])
   i += 1
