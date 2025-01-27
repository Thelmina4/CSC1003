#!/usr/bin/env python3

# s/i = int
# s/o = open square
# eg. n = 3
# ***
# * *
# ***

n = int(input())
i = 0
while i < n:
   if i == 0 or i == n - 1:
      print("*" * n)
   else:
      print("*" + " " * (n - 2) + "*")
   i += 1
