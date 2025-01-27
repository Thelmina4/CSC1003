#!/usr/bin/env python3

# s/i = 1 int
# s/o = diamond
#   *
#  ***
# *****
#  ***
#   *

n = int(input())
i = 0
while i < n:
   if i == n // 2:
      print("*" * n)
   elif i < n // 2:
      space = (" " * (n // 2 - i))
      star = ("*" * ((2 * i) + 1))
      print(space + star)
   else:
      space = (" " * (n // 2 - (n - i - 1)))
      star = ("*" * (2 * (n - i - 1) + 1))
      print(space + star)
   i += 1
