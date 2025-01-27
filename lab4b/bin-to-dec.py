#!/usr/bin/env python3

# s/i = binary number
# s/o = decimal

n = input()
# print(len(n))
decimal = 0

i = 0

while i < len(n):
   binary = int(n[i]) * (2 ** (int(len(n) - i - 1)))
   decimal += binary
   i += 1

print(decimal)
