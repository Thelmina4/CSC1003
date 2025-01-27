#!/usr/bin/env python3

# s/i = seq of str, terminated w "end"
# s/o = str sorted a -> z

s = input()
a = []

while s != "end":
   a.append(s)
   s = input()

i = 0
while i < len(a):
   p = i
   j = p + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   print(a[i])
   i += 1
