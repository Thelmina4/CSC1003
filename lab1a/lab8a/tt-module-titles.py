#!/usr/bin/env python3

# s/i = timetables.txt, terminated w end

# s/o = the modules titles

# 1 10 1 ca277 lg26 Programming Fundamentals

s = input()
# s = s.split()
# print(s)
# s = s[5:]
# s = s.join()
# print(s)
while s != "end":
   s = s.split()
   print(" ".join(s[5:]))
   s = input()
