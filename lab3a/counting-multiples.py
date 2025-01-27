#!/usr/bin/env python3

# s/i = 2 ints, n , m
# s/o = the first n multiples of m

n, m = int(input()), int(input())
# experimenting print(n, m)
i = 0

while i < n:
   print((i + 1) * m)
   i += 1
