#!/usr/bin/env python3

# s/i = int n

# fizz-buzz
# print fizz - multples of 3
# print buzz - multiples of 5
# print fizz-buzz multilples of 3 & 5

n = int(input())
i = 0

while i < n:
   if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
      print("fizz-buzz")
   elif (i + 1) % 3 == 0:
      print("fizz")
   elif (i + 1) % 5 == 0:
      print("buzz")
   else:
      print(i + 1)
   i += 1
