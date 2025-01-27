#!/usr/bin/env python3

# s/i = input of 10 lines, eg 12+34
# s/o = the sum of the number, one per line

i = 0
while i < 10:
   s = input()
   j = 0
   while j < len(s) and s[j] != "+":
      j += 1
   left = int(s[:j])
   right = int(s[j + 1:])
   print(left + right)
   i += 1
