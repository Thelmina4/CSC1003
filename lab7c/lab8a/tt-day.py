#!/usr/bin/env python3

# s/i = timetable.txt, terminated w "end"
#     plus an additional int, day

a = []
s = input()
while s != "end":
   a.append(s)
   s = input()

day = int(input())
# print(day)
i = 0
while i < len(a):
   # print(a[i][0])
   if int(a[i][0]) == day:
      print(a[i])
   i += 1
