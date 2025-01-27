#!/usr/bin/env python3

# s/i = 10 ints
# s/o = mutiple all these numbers together

total = 1
n = 10
i = 0
while i < n:
   m = int(input())
   total *= m
   i += 1

print(total)
