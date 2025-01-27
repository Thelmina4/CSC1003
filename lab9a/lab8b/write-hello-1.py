#!/usr/bin/env python3

# there is no s/i

# must write "Hello_world" to a file

message = "Hello world.\n"

file_name = "hello.txt"

with open(file_name, "w") as f:
   f.write(message)
