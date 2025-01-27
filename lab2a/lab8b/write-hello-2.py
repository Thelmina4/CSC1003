#!/usr/bin/env python3

# s/i = command line argv[1]
#       this will be the name of the file to write to

# s/o = the message "hello world\n" in the file

import sys
# file_name = sys.argv[1]
message = "Hello world.\n"

with open(sys.argv[1], "w") as f:
   f.write(message)
