#!/usr/bin/env python3

# s/i = 3 strings
# s/o = longest line only

l1 = str(input())
l2 = str(input())
l3 = str(input())

if len(l1) > len(l2) and len(l1) > len(l3):
   print(l1)
elif len(l2) > len(l1) and len(l2) > len(l3):
   print(l2)
else:
   print(l3)
