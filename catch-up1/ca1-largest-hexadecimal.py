#!/usr/bin/env python3

# s/i = 2 lines of text, each are pos hex no
# letters in hex are lower case
# s/o = the larger of the 2 nos

# a8d2
# a8c2
result = ""
hx1 = input()
hx2 = input()
if len(hx1) < len(hx2):
   print(hx2)
elif len(hx2) < len(hx1):
   print(hx1)
else:
   if hx1 < hx2:
      print(hx2)
   else:
      print(hx1)
