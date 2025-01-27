#!/usr/bin/env python3

# s/i = seq of lines
#      each line = a sentence

# s/o = one word per line
#      sp need to strip, split, print

# NO LOOPS ALLOWED

# READ()

import sys
# read() takes it as one string
lines = sys.stdin.read()
# print(lines)
# split the spaces and join w \n
words = "\n".join(lines.split())

print(words)
