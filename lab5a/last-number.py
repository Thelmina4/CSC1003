#!/usr/bin/env python3

# s/i = single line of txt
# s/o = last full number
# no output when no number in the line

s = input()
i = len(s) - 1
while 0 <= i and not ("0" <= s[i] and s[i] <= "9"):
   i -= 1
num = ""
j = i
while 0 <= j and ("0" <= s[j] and s[j] <= "9"):
   num = s[j] + num
   j -= 1
if 0 <= i:
   print(num)
