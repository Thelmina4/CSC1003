#!/usr/bin/env python3

# s/i = string
# s/o = the firstdigit and its position, i
# it shouldn't do outpit anything if there are no digits

s = input()
i = 0
while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
   i += 1

if i < len(s):
   print(s[i], i)
