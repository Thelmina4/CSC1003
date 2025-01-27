#!/usr/bin/env python3

# year = 12 months,
# months are numbered 1 -> 12,
# days 1 -> 30,
# week starts on monday, & numbered 1 -> 7

# first day is monday

month = int(input())
dom = int(input())
doy = (((month - 1) * 30) + dom)

a = (doy - 1)
b = int(a / 7)
c = b * 7
dow = doy - c

print(doy - c)
