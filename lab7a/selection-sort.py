#!/usr/bin/env python3

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

i = 0
while i < len(a):
   # 1. find the pos of the smallest number
   p = i
   j = p + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1
   # 2. swap it
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   print(a[i])
   i += 1
