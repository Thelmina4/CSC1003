#!/usr/bin/env python3

# s/i = Assume an existing non-empty list a

# s/o = swap the first and lasts elements

# a = [8, 9, 4, 7, 2, 11]

if 2 <= len(a):
   tmp = a[0]
   a[0] = a[len(a) - 1]
   a[len(a) - 1] = tmp

# print(a)
