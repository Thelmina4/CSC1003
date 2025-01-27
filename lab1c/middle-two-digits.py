#!/usr/bin/env python3

# input of 1 x 6 digit number
# print midddle 2 digits

x = int(input())

# for the left middle digit, divide by 1000, int, mod 10, x 10
xl = (int(x / 1000) % 10) * 10
# print(xl)

# for the right middle digit, divide by 100, int, mod 10
xr = (int(x / 100) % 10)
# print(xr)

print(xl + xr)
