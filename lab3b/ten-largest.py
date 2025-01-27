#!/usr/bin/env python3

# s/i = 10 ints, 1 per line
# s/o = the largest number

largest = int(input())
n = 10
i = 0
while i < n - 1:
   m = int(input())
   if largest < m:
      largest = m
   # print(largest)
   i += 1

print(largest)
