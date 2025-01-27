#!/usr/bin/env python3

# s/i = 1 x int
# s/o = factorial to that number

total = 1
n = int(input())
i = 0
while i < n:
   total *= i + 1
   # print(total)
   i += 1

print(total)
