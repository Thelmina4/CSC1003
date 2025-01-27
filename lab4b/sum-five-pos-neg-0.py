#!/usr/bin/env python3

# s/i = unknown no of int, one per line until 0
# s/o = sum of pos and sum of neg, same line

neg_tot = 0
pos_tot = 0

n = int(input())
while n != 0:
   if n < 0:
      neg_tot += n
   else:
      pos_tot += n
   n = int(input())

print(neg_tot, pos_tot)
