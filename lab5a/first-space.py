#!/usr/bin/env python3

# s/i = 1x line of txt
# s/o = the position, i, of the first space
# output -1 if there are no spaces

s = input()
space = True
no_space = -1
i = 0
while i < len(s) and not (s[i] == " "):
   i += 1
if i < len(s) and space:
   print(i)
else:
   print(no_space)
