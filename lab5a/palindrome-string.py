#!/usr/bin/env python3

# s/i = single line, w
# s/o = "palindrome" or nothing
p = "palindrome"
w = input()

half_len = len(w) // 2

left = w[:half_len]
right = ""

# print("input is even")

i = len(w) - 1
# print(half_len)
if len(w) % 2 == 0:
   while half_len <= i:
      right = right + w[i]
      i -= 1
else:
   while half_len < i:
      right = right + w[i]
      i -= 1
if left == right:
   print(p)
