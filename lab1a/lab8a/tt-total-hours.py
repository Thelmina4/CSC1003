#!/usr/bin/env python3

# s/i = timetable.txt, terminated w "end"

# s/o = the total number of hours (third column)

total = 0
s = input()
while s != "end":
   line = s.split()
   hour = int(line[2])
   total += hour
   s = input()

print(total)
