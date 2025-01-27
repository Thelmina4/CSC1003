#!/usr/bin/env python3

# read int
# int is even print n
# int is odd, print 0
# opposite to the last task

# read int
n = int(input())

# is n even or odd
m = (n % 2)
# it's even then mod 2 = 0
# it's odd then mod  2 = 1

# last time, multiplied by m. eg 2 mod 2  = 0, 3 mod 2 = 1
# minus 1, then  0 => -1, 1=> 0
# can't use abs(), so multiply by -1, and then mulitply by n

m = -(m - 1)

print(n * m)
