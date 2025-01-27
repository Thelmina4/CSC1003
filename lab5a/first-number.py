#!/usr/bin/env python3

# s/i = 1 x line of txt
# s/o = the first whole number
# output = nothing is there is no number

s = input()
i = 0
while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
   i += 1
# print(i)

j = i
while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
   # print(j)
   j += 1
if i < len(s):
   print(s[i:j], i)
