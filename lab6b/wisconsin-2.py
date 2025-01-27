#!/usr/bin/env python3

# s/i = the cities from the last task
# s/o = the count of cities in wisconsin

count = 0

s = input()
while s != "end":
   i = 0
   while s[i] != ",":
      i += 1
   if s[i + 1:i + 3] == "WI":
      count += 1
   s = input()
print(count)
