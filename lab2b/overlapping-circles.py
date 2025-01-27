#!/usr/bin/env python3

# s/i = x1, y1, r1, x2, y2, r2
# figure out if the 2 circles overlap
# s/o = yes or no, overlap or not

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

x3, y3 = x1 - x2, y1 - y2
# print(x3, y3, r3)
r3 = (x3 ** 2) + (y3 ** 2)

if ((r1 + r2) ** 2) > r3:
   print("yes")
else:
   print("no")
