#!/usr/bin/env python3

# the max weight for elevator = 500

# s/i = seq of nos, terminated w "end"
#       the numbers are peoples weights

# sort the numbers
# s/o = the max no of people that can go on the elevator
#       their total weight

s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

# sort
i = 0
while i < len(a):
   p = i
   j = p + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   i += 1

# print(a)
# sum the weights till <= 500

total = 0
elevator = 500
i = 0
while i < len(a):
   if (total + a[i]) <= elevator:
      total += a[i]
      pos = i + 1
   i += 1

print(pos, total)
