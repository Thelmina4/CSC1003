#!/usr/bin/env python3

# s/i = 3 x lines, ints
# they are the sides of a triangle
# s/o = True or False -> equilateral?

s1 = int(input())
s2 = int(input())
s3 = int(input())

# eqi = s1 == s2 and s1 == s3 and s2 == s3
print(s1 == s2 and s2 == s3 and s2 == s3)
