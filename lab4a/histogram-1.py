#!/usr/bin/env python3

# s/i = 10 ints, one per line
# look at test.txt
# use python3 histogram-1.py < test.py
# s/o = "*" * int
m = 10
i = 0
while i < m:
   n = int(input())
   print("*" * n)
   i += 1
