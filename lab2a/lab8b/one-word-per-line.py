#!/usr/bin/env python3

# s/i = seq of lines
#      each line = a sentence

# s/o = one word per line
#      sp need to strip, split, print

# NO LOOPS ALLOWED

# READLINES

import sys
lines = sys.stdin.readlines()

lines = " ".join(lines)

print(lines)
