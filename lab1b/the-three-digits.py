#!/usr/bin/env python3

digit = int(input())

hun = int(digit / 100)
print(hun)
dec = (int(digit / 10) % 10)
print(dec)
i = int(digit % 10)
print(i)
