#!/usr/bin/env python3

# s/i = n = int(input())
# s/o = fibonacci sequence from 0 up to n

n = int(input())

i = 0
prev = 0
curr = 1

if curr < n:
   print(prev)
   print(curr)
else:
   print(prev)

while curr < n:
   temp = prev + curr
   prev = curr
   curr = temp
   if temp < n:
      print(temp)
   i += 1
