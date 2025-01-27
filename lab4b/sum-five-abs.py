#!/usr/bin/env python3

# s/i = exactly 5 ints, one per line
# they will be plus and minus
# s/o = sum of the absoute value

total = 0
i = 0

while i < 5:
   n = int(input())
   if n < 0:
      n = -n
      total = total + n
   else:
      total = total + n
   i += 1
print(total)
