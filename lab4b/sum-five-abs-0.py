#!/usr/bin/env python3

# s/i = ints, until you hit a 0
# s/o = sum of the absolute value of the ints

total = 0
n = int(input())

while n != 0:
   if n < 0:
      n = -n
      total += n
      # print(total)
   else:
      total += n
      # print(total)
   n = int(input())

print(total)
