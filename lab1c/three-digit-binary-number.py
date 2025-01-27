#!/usr/bin/env python3

# convert binary to decimal
# take input binary 1,0 x 3
# output that as a no

a = int(input())
b = int(input())
c = int(input())

print((a * (2 ** 2)) + (b * (2 ** 1)) + (c * (2 ** 0)))
