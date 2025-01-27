#!/usr/bin/env python3

# s/i = 10 ints, 1 per line
# s/i = only the smallest no greater than 0

# 0 is not positive
smallest = 0
n = 10
i = 0
while i < n:
   m = int(input())
   # m greater than zero AND
   # smallest is the smallest pos int = 1 or
   # m <= smallest eg. 1
   if m > 0 and (smallest == 0 or m <= smallest):
      smallest = m
   i += 1

print(smallest)
