#!/usr/bin/env python3

# s/i = the cities from the last 2 tasks,
# look at cities-1 txt
# terminated w "end"

# s/o = only the cities that are called SOMETHING city
# eg, Valley City, Salt Lake City

s = input()
s = input()
while s != "end":
   i = 0
   while s[i] != ",":
      i += 1
   if s[i - 4:i] == "City":
      print(s[:i])
   s = input()
