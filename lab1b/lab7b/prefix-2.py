#!/usr/bin/env python3

# Assume an existing list of words (strings) a
# and another str s

# s/o = writes the first word in a for which s is a prefix

# a = ['mountain', 'montagne', 'mont', 'mo', 'montages', 'zebra', 'monthly']
# s = "mont"
# montagne

# a = ['ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
# s = "abc"
# abc

# a = ['dog', 'cat', 'mouse']
# s = ""
# dog
# print(type(s))
a = []
s = "mongoose"

# a = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
# s = 1
# 10


i = 0
while len(a) > 0 and i < len(a) and a[i][:len(s)] != s:
   i += 1

if len(s) == 0:
   print(a[0])
elif i < len(s):
   print(a[i])
elif len(a) == 0:

if __name__ == "__main__":
   a = ["dog", "cat", "mouse"]
