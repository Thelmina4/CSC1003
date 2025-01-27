#!/usr/bin/env python3

# s/i = 2 ins, n & m
# s/o = n terms of the hailstones sequence begining w m

n, m = int(input()), int(input())
print(m)
i = 0
while i < n - 1:
   if m % 2 == 0:
      m = m // 2
      print(m)
   elif m % 2 == 1:
      m = (m * 3) + 1
      print(m)
   # print(i)
   i += 1
