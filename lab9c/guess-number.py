#!/usr/bin/env python3

import secret

#
# Use linear-search to find the secret number. This will (nearly
# always) fail because we are only allowed 10 guesses.
#
min = 0
max = 1000

high = "too-high"
low = "too-low"

mid = (min + max) // 2
value = secret.guess(mid)
while value != "correct":
   if value == high:
      max = mid
      # print(mid)
      mid = (min + max) // 2
   elif value == low:
      min = mid
      mid = (min + max) // 2
   value = secret.guess(mid)
   # print("end", min, mid, max)
