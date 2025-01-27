#!/usr/bin/env python3

# s/i = one line, eg 271+9730+30+813+5

# s/o = the sum of the numbers eg,10849

s = input()
tmp = 0
total = 0
i = 0

while i < 5:
   j = tmp
   while j < len(s) and s[j] != "+":
      j += 1
   total += int(s[tmp:j])
   tmp = j + 1
   # print("total:", total, "tmp:", tmp)
   i += 1

print(total)
