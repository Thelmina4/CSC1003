#!/usr/bin/env python3

# s/i = int
# s/o = cross
# eg n = 5
#   *
#   *
# *****
#   *
#   *

n = int(input())
i = 0
while i < n:
   if i == n // 2:
      print("*" * n)
   else:
      print(" " * (n // 2) + "*")
   i += 1
