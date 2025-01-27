#!/usr/bin/env python3

# s/i = 10 ints, one per line
# s/o = the smallest number

smallest = int(input())
n = 10
i = 0
while i < n - 1:
   m = int(input())
   if m < smallest:
      smallest = m
      # print(smallest)
   i += 1

print(smallest)
