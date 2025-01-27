#!/usr/bin/env python3

# s/i = int
# s/o = diagonal cross
# eg n = 5
# *   *
#  * *
#   *
#  * *
# *   *

n = int(input())
i = 0

while i < n:
   if i < n // 2:
      print((" " * i) + "*" + (" " * (n - (i * 2) - 2) + "*"))
   elif i > n // 2:
      print((" " * (n - i - 1)) + "*" + (" " * ((i * 2) - n) + "*"))
   else:
      print(" " * (n // 2) + "*")
   i += 1
