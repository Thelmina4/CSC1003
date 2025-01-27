#!/usr/bin/env python3

# input = current working directory has a file
#        irish-dobs txt
#        lines of txt eg 8/1/35 elvis P

# output= americanised dates -> american-dobs.txt

# readlines() turns it into a list of strings,
# each line is a string

with open("irish-dobs.txt") as f:
   lines = f.readlines()
a = []
# print(lines)
i = 0
while i < len(lines):
   # remove the \n
   toks = lines[i].rstrip()
   toks = toks.split("/")
   # print(toks)

   tmp = toks[0]
   toks[0] = toks[1]
   toks[1] = tmp
   toks = "/".join(toks)
   # print(toks)
   a.append(toks)
   i += 1
# print(a)
with open("american-dobs.txt", "w") as f:
   line = "\n".join(a) + "\n"
   f.write(line)
