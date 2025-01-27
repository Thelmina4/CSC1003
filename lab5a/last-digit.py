#!/usr/bin/env python3

# s/i = 1 x line of txt
# s/o = the last digit
# no putput if there are no numbers

s = input()
i = len(s) - 1

while 0 <= i and not ("0" <= s[i] and s[i] <= "9"):
   i -= 1
if 0 <= i:
   print(s[i])
