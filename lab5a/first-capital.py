#!/usr/bin/env python3

# s/i= single line of text
# s/o = the first cap in the line and it's pos i
# output nothing if there is no cap
s = input()

i = 0
while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
   i += 1
if i < len(s):
   print(s[i], i)
