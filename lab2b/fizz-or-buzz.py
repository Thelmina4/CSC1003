#!/usr/bin/env python3

# s/i = 1 * int
# fizz-buzz =
# x / 3 == fizz
# int / 5 == buzz
# int / 3 & 5 == fizz buzz
# else print (x)

x = int(input())

if x % 3 == 0 and x % 5 == 0:
   print("fizz-buzz")
elif x % 3 == 0:
   print("fizz")
elif x % 5 == 0:
   print("buzz")
else:
   print(x)
