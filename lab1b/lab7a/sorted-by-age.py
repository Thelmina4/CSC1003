#!/usr/bin/env python3

# s/i = seq of lines, terminated w "end"
# the line is DOB and name

# s/o = the name of the person, sorted by dob

s = input()
a = []
while s != "end":
   a.append(s)
   s = input()

# b = "08/01/25"
# year = b[6:8]
# month = b[3:5]
# day = b[0:2]
# print(year, month, day)
i = 0
while i < len(a):
   p = i
   j = p + 1
   while j < len(a):
      yj = int(a[j][6:8])
      yp = int(a[p][6:8])
      mj = int(a[j][3:5])
      mp = int(a[p][3:5])
      dj = int(a[j][:2])
      dp = int(a[p][:2])

      if yj < yp:
         p = j
      elif yj == yp and mj < mp:
         p = j
      elif yj == yp and mj == mp and dj < dp:
         p = j
      j += 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   print(a[i][9:])
   i += 1
