#!/usr/bin/env python3

# bin to dec

s = input()
binary = 0
power = 0
i = 0
while i < len(s):
   if int(s) <= 2 ** i:
      power = 2 ** i
   
