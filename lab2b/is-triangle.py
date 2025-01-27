#!/usr/bin/env python3

# s/i 3 lines of ints
# they are the 3 sides of a possible triangle
# figure out if they can for a triangle or not

a = int(input())
b = int(input())
c = int(input())

# Triangle: sum of any 2 sides are greater than 3rd
# its a triangle

if c < (a + b) and b < (a + c) and a < (c + b):
   print("yes")
else:
   print("no")
