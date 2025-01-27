#!/usr/bin/env python3

# input is a 2 digit no
# print the 2 digits, eg. 75 = 12

# left no is int ( / 10)
# right no is mod 10

x = int(input())
xl = int(x / 10)
xr = x % 10
# print(xl, xr)

print(xl + xr)
