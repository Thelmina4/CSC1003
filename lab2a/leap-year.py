#!/usr/bin/env python3

# s/i = int of a year
# s/o = boolean True or False -> leap year

year = int(input())

print((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))
