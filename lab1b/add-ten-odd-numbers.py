#!/usr/bin/env python3

# input = 10 ints, 1 per line
# add only the odd numbers

# in 10 again, we took the total = total + int(input())
# find odd only and add to total

# declare variable

total = 0

# in odd-value-or-zero, printed odd
a = int(input())
m = (a % 2)
total = total + (a * m)

b = int(input())
m = (b % 2)
total = total + (b * m)

c = int(input())
m = (c % 2)
total = total + (c * m)

d = int(input())
m = (d % 2)
total = total + (d * m)

e = int(input())
m = (e % 2)
total = total + (e * m)

f = int(input())
m = (f % 2)
total = total + (f * m)

g = int(input())
m = (g % 2)
total = total + (g * m)

h = int(input())
m = (h % 2)
total = total + (h * m)

i = int(input())
m = (i % 2)
total = total + (i * m)

j = int(input())
m = (j % 2)
total = total + (j * m)

print(total)
