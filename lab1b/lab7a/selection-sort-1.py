#!/usr/bin/env python3

# s/i = seq of nos, terminated w "end"
# s/o = the position of the smallest no

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

# print(type(a[0]))

pos = 0
i = 1
while i < len(a):
   if a[i] < a[pos]:
      pos = i
   i += 1

print(pos)
