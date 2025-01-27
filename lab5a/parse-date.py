#!/usr/bin/env python3

# s/i = Tuesday 23rd October, 2018
# s/o = October 23rd, 2018 (Tuesday)


# day = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
s = input()

i = 0
while i < len(s) and not s[i] == " ":
   i += 1
day = s[:i]
j = i + 1
# print(day, s[j])
while j < len(s) and not s[j] == " ":
   j += 1
date = s[i + 1:j]
a = j + 1
while a < len(s) and not s[a] == " ":
   a += 1
month = s[j + 1:a - 1]
year = s[a + 1:]
print(month, date + ",", year, "(" + day + ")")
