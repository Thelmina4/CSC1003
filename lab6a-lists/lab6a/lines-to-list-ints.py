#!/usr/bin/env python3

# s/i = seq of ints, terminated w "end"

# s/o = the line

a = []
n = input()
while n != "end":
   a.append(int(n))
   n = input()

print(a)
