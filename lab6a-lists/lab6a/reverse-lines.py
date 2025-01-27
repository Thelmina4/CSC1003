#!/usr/bin/env python3

# s/i = seq of lines, terminaated w "end"
# s/o = those lines in reverse order

a = []

n = input()
while n != "end":
   a.append(n)
   n = input()

if len(a) != 0:
   i = 0
   while i < len(a):
      print(a[len(a) - i - 1])
      i += 1
