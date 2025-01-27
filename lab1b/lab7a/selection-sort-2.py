#!/usr/bin/env python3

# s/i = seq of ints, terminated "end"
# s/i = a furter int , i

# s/o = the POSITION of thesmallest int between i and the eol

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

pos = int(input())
i = pos + 1
while i < len(a):
   if a[i] < a[pos]:
      pos = i
   i += 1

print(pos)
