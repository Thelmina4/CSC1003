#!/usr/bin/env python3

# s/i = 2 dates, one per line
#      eg 10/1

# 1st date is earlier
# 2nd date is later

# s/o = no of days bewteen the 2 dates

import sys
dates = sys.stdin.read().split()
date1, date2 = dates[0].split("/"), dates[1].split("/")
# print(date1, date2)
start_day, start_mon = int(date1[0]), int(date1[1])
end_day, end_mon = int(date2[0]), int(date2[1])

months = [31] * 13

months[0], months[2] = 0, 28
months[4], months[6], months[9], months[11] = 30, 30, 30, 30
# print(months)

print
