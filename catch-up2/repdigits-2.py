#!/usr/bin/env python3

# s/i = seq of 2 digit numbers
# s/o = only the first digit which is a repdigit

n = int(input())
if n // 10 == n % 10:
   print(n)
else:
   while not (n // 10 == n % 10):
      n = int(input())
      if n // 10 == n % 10:
         print(n)
