#!/usr/bin/env python3

# s/i = 2 positive ints, one per line, n , p
# s/o = the pth digit of n
# eg 9876
# 6 = 0th digit
# 7 = 1st digit
# 8 = 2nd digit
# 9 = 3rd digit

# long Number
n = int(input())
# pth digit of that number
p = int(input())

print(n // (10 ** p) % 10)
