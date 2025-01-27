#!/usr/bin/env python3

# s/i = 5 ints, one per line
# s/o = 2 ints, on same line
# one neg, one pos

neg_tot = 0
pos_tot = 0
i = 0

while i < 5:
   n = int(input())
   if n < 0:
      neg_tot += n
   else:
      pos_tot += n
   i += 1

print(neg_tot, pos_tot)
