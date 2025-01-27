#!/usr/bin/env python3

# s/i =lines from timetable.txt,
#      terminated w "end"

# s/o = the module code
# eg
# 1 10 1 ca277 lg26 Programming Fundamentals I

s = input()
while s != "end":
   print(s[7:12])
   s = input()
