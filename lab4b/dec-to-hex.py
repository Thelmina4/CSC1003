#!/usr/bin/env python3

# s/i = int - dec
# s/o = dec to hex

dec = int(input())
hx = "0123456789abcdef"

i = 0
while 16 ** i < dec:
   power = i
   i += 1
# print(power, i)

h = ""

while i > 0:
   hi = dec // (16 ** power)
   h = h + hx[hi]
   dec = dec % (16 ** power)
   power -= 1
   i -= 1

print(h)
