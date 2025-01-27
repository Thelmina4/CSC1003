#!/usr/bin/env python3

# s/i = seq of lines, terminated w "end"

# s/o = the line with the extra spaces removes,
#       each new line will end w "."
lines = []
b = ""
s = input()
while s != "end":
   b = b + s
   lines.append(s)
   s = input()

text = " ".join(lines)

# print("a:", text)
# print("b:", b)

sentences = text.split(".")
#print(sentences)

i = 0
while i < len(sentences):
   line = sentences[i].split()
   line = " ".join(line)
   # print(line)
   if 0 < len(line):
      print(line + ".")
   i += 1
