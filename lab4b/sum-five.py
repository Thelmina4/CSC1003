#!/usr/bin/env python3

# s/i = read 5 ints, one per line
# s/o = sum of the ints

total = 0
i = 0
while i < 5:
   n = int(input())
   total = total + n
   i += 1

print(total)
