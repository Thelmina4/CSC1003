#!/usr/bin/env python3

# hailstones
# s/i = int
# s/o = next line in hailstones

n = int(input())

# IF n is even: divide by 2
# ELSE : MULTIPLY BY 3 AND ADD ONE

if n % 2 == 0:
   print(n // 2)
else:
   print((3 * n) + 1)
