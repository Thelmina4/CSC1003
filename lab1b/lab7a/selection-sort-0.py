#!/usr/bin/env python3

# s/i = seq of numbers, teminated w "end"
# put into list

# s/o = the smallest number
n = input()
a = []
i = 0
while n != "end":
   a.append(int(n))
   n = input()
   i += 1
# print(type(a[0]))
smallest = a[0]
j = 1
while j < len(a):
   if a[j] < smallest:
      smallest = a[j]
   j += 1

print(smallest)
