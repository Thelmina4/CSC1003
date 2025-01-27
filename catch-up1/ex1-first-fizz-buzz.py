#!/usr/bin/env python3

# s/i = seq of numbers, 1 / line
# s/o = fizzbuzz


n = int(input())
if n % 3 == 0 and n % 5 == 0:
   print(n)
else:
   while not (n % 3 == 0 and n % 5 == 0):
      n = int(input())
      if n % 3 == 0 and n % 5 == 0:
         print(n)
