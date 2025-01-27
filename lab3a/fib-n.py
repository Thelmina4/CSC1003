#!/usr/bin/env python3

# s/i = int(input())
# s/o = first n terms of the fibonacci seq

# fib seq = sum of the 2 prev numbers = next number

n = int(input())
i = 0
prev = 0
curr = 1
print(prev)
print(curr)
while i < n - 2:
   temp = prev + curr
   prev = curr
   curr = temp
   print(temp)
   # print("i = ", i)
   i += 1
