#!/usr/bin/env python3

# s/i = reads unknow no of ints
# stops when it gets a 0
# s/o = sum of the ints

total = 0
n = int(input())
while n != 0:
   total = total + n
   n = int(input())

print(total)
