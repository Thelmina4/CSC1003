#!/usr/bin/env python3

# s/i = single line of text,s
# s/o = number of caps

# Nobody expects the Spanish Inquisition!

s = input()

total = 0
i = 0
while i < len(s):
   if "A" <= s[i] and s[i] <= "Z":
      total += 1
   i += 1

print(total)
