#!/usr/bin/env python3

# year = 12 months,
# months are numbered 1 -> 12,
# days 1 -> 30,
# week starts on monday, & numbered 1 -> 7

# standard input of 2 ints, month no & day of the month

# print the day of the year
# days of the year are numbered 1 -> 360

month = int(input())
dom = int(input())
doy = (((month - 1) * 30) + dom)

print(doy)
