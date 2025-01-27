#!/usr/bin/env python3

# s/i = seq of nums, terminated w end
# s/o = the repdigit, if there is one

n = input()
if n != "end" and int(n) // 10 == int(n) % 10:
   print(n)
else:
   while n != "end" and not (int(n) // 10 == int(n) % 10):
      n = input()
      if int(n) // 10 == int(n) % 10:
         print(n)
