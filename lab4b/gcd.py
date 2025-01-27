#!/usr/bin/env python3

# s/i = 2 ints, one per line
# s/o = the greatest common divisor
# eg 75, 30 = 15

a = int(input())
b = int(input())

while b != 0:
   c = a % b
   a = b
   b = c

print(a)
