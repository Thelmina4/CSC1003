#!/usr/bin/env python3

# s/i = int, that's < 20
# s/o = print or not prime

n = int(input())

if n == 2 or n == 3 or n == 5 or n == 7:
   print("prime")
elif n == 11 or n == 13 or n == 17 or n == 19:
   print("prime")
else:
   print("not prime")
