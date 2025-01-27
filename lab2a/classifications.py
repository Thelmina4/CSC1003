#!/usr/bin/env python3

# s/i = int, student grade
# >= 70% == 1st
# >= 50 and <= 69 == second
# >= 40% and <= 49 == third
# < 40% == fail

# s/o = boolean the grades in 4 lines

grade = int(input())
print("first:", (grade >= 70))
print("second:", grade >= 50 and grade <= 69)
print("third:", grade >= 40 and grade <= 49)
print("fail:", grade < 40)
