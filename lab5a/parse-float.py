#!/usr/bin/env python3

# s/i = single line of txt w a floating point, f = input()
# s/o = the integer on one line and the f on the other

f = input()
i = 0
while i < len(f) and not (f[i] == "."):
   i += 1

print(f[:i])
print(f[i + 1:])
