#!/usr/bin/env python3

# 2 ints, 1st = no rabbits, 2nd  = no years
# rabbits dbl every year.
# how amny rabbits after years?

rabbits = int(input())
years = int(input())

rabbits = (rabbits * (2 ** years))
print(rabbits)
