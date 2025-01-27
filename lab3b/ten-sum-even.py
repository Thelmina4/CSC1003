#!/usr/bin/env python3

# s/i = 10 numbers
# s/o = sum of the even numbers

total = 0

n = 10
i = 0
while i < n:
   m = int(input())
   if m % 2 == 0:
      total += m
   i += 1

print(total)
