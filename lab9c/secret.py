#!/usr/bin/env python3
# secret.py
#
import random
# The secret number is in the range [0,999], inclusive.
#
maximum = 999
secret = random.randint(0,maximum)
# Maximum ten guesses.
#
N = 10
guesses = N
correct = False
# Show the secret on stdout.
#
print("secret:", secret)

# Make a guess by calling this function with your guess, n. You may
# call this function a maximum of N (10) times.
#

def guess(n):
   global guesses, correct
   guesses -= 1
   print("guess {} (guess {} of {}, {} remaining)".format(n, N - guesses, N, guesses))
   if guesses < 0:
      raise Exception("error: too many guesses")
   correct = (n == secret)
   if n < secret:
      return "too-low"
   elif secret < n:
      return "too-high"
   else:
      return "correct"
