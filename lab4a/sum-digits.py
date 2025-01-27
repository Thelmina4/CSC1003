#!/usr/bin/env python3

# s/i = string
# convert string to int
# s/o = sum of all the digits

s = input()

# print(int(s[0]) + int(s[1]))

total = 0
i = 0

while i < len(s):
   total = total + int(s[i])
   i += 1

print(total)
