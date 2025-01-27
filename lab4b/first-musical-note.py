#!/usr/bin/env python3

# musical notes = a - > g
# s/i = string, one line
# s/o = the first time an "a" - "g" in sentence

s = input()
i = 0
while not (s[i] >= "a" and s[i] <= "g"):
   i += 1

print(s[i])
