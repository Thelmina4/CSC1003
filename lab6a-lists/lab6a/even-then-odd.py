#!/usr/bin/env python3

# s/i = seq on ints, terminated w "end"

# s/o = even nos, then the odds
# need to put the odds into a list,
# and just print even as it comes

odds = []

n = input()
while n != "end":
   if int(n) % 2 == 0:
      print(n)
   else:
      odds.append(n)
   n = input()

i = 0
while i < len(odds):
   print(odds[i])
   i += 1
