#!/usr/bin/env python3

# s/i = int
# s/o = st, nd, rd, th

n = int(input())
# print(n)
if n < 21 and n > 3:
   print("th")
elif n % 10 == 1:
   print("st")
elif n % 10 == 2:
   print("nd")
elif n % 10 == 3:
   print("rd")
else:
   (print("th"))
