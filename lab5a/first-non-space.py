#!/usr/bin/env python3

# s/i = 1 x line of txt
# s/o = pos of the first NON space
# output = -1 if there are no non spaces

s = input()

no_space = -1
i = 0
while i < len(s) and s[i] == " ":
   i += 1

if i < len(s) and i != 0:
   print(i)
else:
   print(no_space)
