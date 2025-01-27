#!/usr/bin/env python3

# s/i = the header from cities txt
# eg City,State,LatD,LatM,LatS,NS,LonD,LonM,LonS,EW

# s/o = each part, one per line

s = input()

tmp = 0
i = 0
while i < len(s):
   j = tmp
   while j < len(s) and s[j] != ",":
      j += 1
   if s[tmp:j] != "":
      print(s[tmp:j])
   tmp = j + 1
   i += 1
