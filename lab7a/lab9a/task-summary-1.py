#!/usr/bin/env python3

# s/i = seq of lines eg
# count-up-to-odd.py.incorrect
# count-up-to.py.correctadd.py.incorrect
# concat-lines.py.correct
# add.py.correct
# count-up-to-odd.py.correct
# add.py.incorrect
# less-than.py.correct

# a task is correct only if the last upload for the task is "correct"

# s/o = only thr script name if it was correct

import sys

scripts = sys.stdin.readlines()
# print(scripts)
dict = {}
i = 0
while i < len(scripts):
   line = scripts[i].rstrip().split(".")
   #script = line[0] + "." + line[1]
   script = ".".join(line[:2])
   val = line[2]
   # print(script, val)
   if script not in dict:
      dict[script] = val
   else:
      dict[script] = val

   i += 1
# print(dict)
for script in dict:
   if dict[script] == "correct":
      print(script)
