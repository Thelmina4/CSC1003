#!/usr/bin/env python3

# s/i = w & h
# s/o = underweight, normal, over, obese

w = int(input())
h = int(input())
h = h / 100
bmi = w / (h * h)
# print(bmi)

if bmi < 18.5:
   print("underweight")
elif bmi >= 18.5 and bmi < 25:
   print("normal")
elif bmi >= 25.0 and bmi < 30:
   print("overweight")
elif bmi >= 30.0:
   print("obese")
