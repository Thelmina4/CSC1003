#!/usr/bin/env python3

# s/i = ints, 1 /line, until 0
# s/o = higher, lower, equal

prev = int(input())
if prev != 0:
   curr = int(input())
   while curr != 0:
      if curr < prev:
         print("lower")
      elif curr > prev:
         print("higher")
      else:
         print("equal")
      prev = curr
      curr = int(input())
