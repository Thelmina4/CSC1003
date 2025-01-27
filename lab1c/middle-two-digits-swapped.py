#!/usr/bin/env python3

# same as last one, print only middle 2 digits
# Except swap them

x = int(input())

# for the left middle, divide by 1000, int, mod 10
xl = (int(x / 1000) % 10)
# for the rigt middle, divide by 100, int, mod 10, X 10
xr = (int(x / 100) % 10) * 10
print(xl + xr)
