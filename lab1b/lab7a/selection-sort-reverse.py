#!/usr/bin/env python3

# s/i = seq on ints, terminated "end"
# s/0 = sort into decreasing order

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

i = 0
while i < len(a):
   p = i
   j = p + 1
   while j < len(a):
      if a[p] < a[j]:
         p = j
      j += 1

   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   print(a[i])
   i += 1
