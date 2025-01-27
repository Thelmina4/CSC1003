#!/usr/bin/env python3

# s/i = 3 ints, one per line
# a, b & c
# s/o = print(a) -> c is even, or print(b)-> c odd

a = int(input())
b = int(input())
c = int(input())
# c is even c % 2 == 0
# c is odd c % 2  == 1
# reverse it, make mod 2 == 1 for even, mod 2 == 0 for odd
# multiply 1st no w 1 (even), second number w 0 (odd).
# add the result
print(a * ((c + 1) % 2) + b * (c % 2))
