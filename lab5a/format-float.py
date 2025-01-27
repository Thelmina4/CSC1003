#!/usr/bin/env python3

# s/i = a number, could be pos or neg
# maybe interger or floating point
# floating p might not have an integer or the fraction part
# there's no white spaces

# s/o = the same number with both the integer and the floating p
# 4 possibilities
# .2
# 12
# 12.
# 12.34

s = input()
if s < 0:
   t = s * -1
else:
   t = s
if t[0] == ".":
   # .12
   # first pos is .
   print("0" + s)
elif s[len(s) - 1] == ".":
   # 12.
   # last pos is .
   print(s + "0")
else:
   i = 0
   while i < len(s) and ("0" <= s[i] and s[i] <= "9"):
      # doesn't start or end w a .
      # run thru the line while its a number
      i += 1
   j = i
   # print(j)
   # print(len(s))
   if j == len(s):
      # 12
      # end of line and i is a number
      print(s + ".0")
   elif s[j] == ".":
      print(s)
