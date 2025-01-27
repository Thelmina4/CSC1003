#!/usr/bin/env python3

# s/i = 10 ins, one per line
# s/o = "odd" or "even"

i = 0
while i < 10:
   n = int(input())
   if n % 2 == 0:
      print("even")
   else:
      print("odd")
   i += 1
