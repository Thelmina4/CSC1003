#!/usr/bin/env python3

# s/i = read 6 ints, one per line
# s/o = higher lower equal

# n = int(input())
prev = int(input())
curr = 0
i = 0
while i < 5:
   curr = int(input())
   if curr > prev:
      print("higher")
   elif curr < prev:
      print("lower")
   else:
      print("equal")
   prev = curr
   i += 1
