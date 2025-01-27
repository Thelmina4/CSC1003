#!/usr/bin/env python3

# s/i = 1 x pos int, n
# convert it to hx

# s/o = the fist letter in the hx no
# no letter = no s/o

n = int(input())
s = ""
digits = "0123456789abcdef"

# Convert integer to hexadecimal string

while 0 < n:
   s = digits[n % 16] + s
   n = n // 16
# Linear search to find the first hexadecimal letter

i = 0
while i < len(s) and not ("a" <= s[i] and s[i] <= "f"):
   i = i + 1
if i < len(s):
   print(s[i])
