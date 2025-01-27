#!/usr/bin/env python3

# s/i = timetable.txt, terminated w "end"

# s/o = the stert time and end time in 24 hour clock
# eg 1 10 1 ca277 lg26 Programming
# eg - 1 11 2 ca222 qg27 Enterprise Information Systems
# turns into

# 1 11:00 12:50 ca222 qg27 Enterprise Information Systems

s = input()

while s != "end":
   line = s.split()
   start = int(line[1])
   line[1] = str(start) + ":00"
   duration = int(line[2])
   end_hour = (start + duration - 1) % 24
   line[2] = str(end_hour) + ":50"

   print(" ".join(line))
   s = input()
