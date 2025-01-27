#!/usr/bin/env python3

# s/i = seq of ints, one / line
#       THERE IS NO "END"
# s/o = sum to s/o

import sys

total = 0
line = sys.stdin.readline()
while 0 < len(line):
   total += int(line)
   line = sys.stdin.readline()

print(total)
