#!/usr/bin/env python3

# s/i = 10 ints
# s/o = sum of the positive numbers

total = 0
n = 10
i = 0
while i < n:
   m = int(input())
   if 0 < m:
      total += m
   i += 1

print(total)
