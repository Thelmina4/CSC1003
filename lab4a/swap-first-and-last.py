#!/usr/bin/env python3

# s/i = string
# s/o = swap the first and last letters

s = input()
print(s[len(s) - 1] + s[1:len(s) - 1] + s[0])
