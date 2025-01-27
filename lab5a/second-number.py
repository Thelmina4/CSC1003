#!/usr/bin/env python3

# s/ = 1 x line of txt
# s/o = the SECOND number
# no output if there is no second number
s = input()
i = 1
# get the position of the first number
while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
   i += 1
# make j the same position as i, get the end of the no
j = i
while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
   j += 1
if i < len(s):
   k = j
   #print(s[k])
   while k < len(s) and not ("0" <= s[k] and s[k] <= "9"):
      k += 1
   n = k
   while n < len(s) and ("0" <= s[n] and s[n] <= "9"):
      n += 1
   if k < len(s):
      print(s[k:n], k)
