#!/usr/bin/env python3

# input are 2 txts, boys.txt & girls.txt

# s/o = the name and the gender
#       "boy" / "girl" / "either"

import os
import sys

b = "boys.txt"
gl = "girls.txt"

with open(b, "r") as f, open(gl, "r") as g:
   boys = f.read().strip().split()
   girls = g.read().strip().split()
# print(boys, "\n", girls)
boy_name = {}
girl_name = {}

i = 0
while i < len(boys):
   boy_n = boys[i]
   # print(boy_n)
   boy_name[boy_n] = "boy"
   i += 1

i = 0
while i < len(girls):
   girl_n = girls[i]
   girl_name[girl_n] = "girl"
   i += 1

names = sys.stdin.readlines()

j = 0
while j < len(names):
   name = names[j].rstrip()
   if name in boy_name and (name in girl_name):
      print(name, "either")
   if name in boy_name and name not in girl_name:
      print(name, "boy")
   if name in girl_name and name not in boy_name:
      print(name, "girl")
   j += 1
