#!/usr/bin/env python3

# s/i = int
# s/o = diagonal *
# eg n = 3
# *
#  *
#   *

n = int(input())

i = 0
while i < n:
   print((" " * i) + "*")
   i += 1
