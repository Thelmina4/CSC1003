#!/usr/bin/env python3

# s/i = 1 int n, followed by n 2 digit numbers
# s/o = only the pairs

n = int(input())
i = 0
while i < n:
   num = int(input())
   # left = num // 10
   # right = num % 10
   if num // 10 == num % 10:
      print(num)
   i += 1
