#!/usr/bin/env python3

# s/i = sq of ints, m, terminated w "end"
# and then followed by one further int , n

# s/o = m + n, one per line

a = []
m = input()
while m != "end":
   a.append(int(m))
   m = input()

n = int(input())
i = 0
while i < len(a):
   print(a[i] + n)
   i += 1
