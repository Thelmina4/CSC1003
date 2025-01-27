#!/usr/bin/env python3

# s/i = int
# s/o = triangle
# eg n = 3
# *
# **
# ***

n = int(input())
i = 0
while i < n:
   print("*" * (i + 1))
   i += 1
