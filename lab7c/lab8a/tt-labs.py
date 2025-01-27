#!/usr/bin/env python3

# s/i = timetable.txt, terminated w "end"

# s/o = ONLY THE labs
#       the lectures are 1 hour
#       the labs are > 1 hour

s = input()
while s != "end":
   line = s.split()
   hour = int(line[2])
   if hour > 1:
      print(s)
   s = input()
