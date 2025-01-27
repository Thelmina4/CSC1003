#!/usr/bin/env python3

# s/i = seq of numbers, terminated w "end"
# s/o = te median of the numbers

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
      if a[j] < a[p]:
         p = j
      j += 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   i += 1
print(a[len(a) // 2])
# print(a)
