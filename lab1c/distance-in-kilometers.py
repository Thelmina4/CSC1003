#!/usr/bin/env python3

# input is km
# divide it by 1
x = int(input())
# add 500 to x. if it does move you past the next int
# eg. 1499 + 500 = 1999
# that double divided by 1000, is 1
# // means it's an int, not float
r = ((x + 500) // 1000)

print(r)
