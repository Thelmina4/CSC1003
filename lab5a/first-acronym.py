#!/usr/bin/env python3

# s/i = 1 x line of text
# s/o = the first acronym and its pos, i ,
# s/o = nothing if there is no acronym
# acronym = caps

s = input()
i = 0
while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
   i += 1

j = i
while j < len(s) and ("A" <= s[j] and s[j] <= "Z"):
   j += 1

if i < len(s):
   print(s[i:j], i)
