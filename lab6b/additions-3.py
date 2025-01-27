#!/usr/bin/env python3

# s/i = seq of additions, one per line
# eg, 12+45
# s/o = the sum of each line, one per line
# stop at 1000

total = 0
while total != 1000:
   s = input()
   i = 0
   while i < len(s) and s[i] != "+":
      i += 1
   total = int(s[:i]) + int(s[i + 1:])
   print(total)
