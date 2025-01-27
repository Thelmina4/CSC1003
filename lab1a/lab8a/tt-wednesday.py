#!/usr/bin/env python3

# s/i = timetable.txt, terminated w "end"

# s/o = the days that are wednesday, first token is 3

wed = 3

s = input()
while s != "end":
   toks = s.split()
   # print(toks[0])
   if int(toks[0]) == wed:
      print(s)
   s = input()
