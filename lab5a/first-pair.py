#!/usr/bin/env python3

# s/i = 1 x line of txt
# s/o = pair of contiguous characters
# or nothing if no pairs

s = input()
i = 0
j = 1
while j < len(s) and not (s[i] == s[j]):
   i += 1
   j += 1

if j < len(s) and (s[i] == s[j]):
   print(s[i:i + 2])
