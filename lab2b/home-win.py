#!/usr/bin/env python3

# s/i = 2 lines of ints
# first = home, second = away
# s/o = Home win., Draw., Away win.

home = int(input())
away = int(input())

if home == away:
   print("Draw.")
elif home > away:
   print("Home win.")
else:
   print("Away win.")
