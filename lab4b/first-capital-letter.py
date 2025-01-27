#!/usr/bin/env python3

# s/i = string, one line
# s/o = the position where the first cap is

s = input()

i = 0
while not ("A" < s[i] and s[i] < "Z"):
   i += 1

print(i)
