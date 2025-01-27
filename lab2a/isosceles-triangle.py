#!/usr/bin/env python3

# s/i = 3 lines of ints
# legths of the sides of a triangle
# s/o True or False - > isisceles triangle
# isoceles triangle = 2 x sides of equal length

s1 = int(input())
s2 = int(input())
s3 = int(input())

print(s1 == s2 or s1 == s3 or s2 == s3)
