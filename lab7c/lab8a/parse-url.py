#!/usr/bin/env python3

# s/i = URI = scheme ":" ["//" authority] path ["?" query] ["#" fragment]

# s/o = scheme: https
#       host: projects.computing.dcu.ie
#       port: 443
#       path: /project.html
#       query-string: module=ca400&mine&user=mousem2
#       fragment-id: bottom

import sys
url = sys.argv[1]
# print(url)

toks = url.split("/")
# print(toks)
scheme = toks[0].split(":")
print("scheme: " + scheme[0])

host_port = toks[2].split(":")
# print(host_port)
if len(host_port) == 2:
   print("host: " + host_port[0] + "\nport: " + host_port[1])
else:
   print("host: " + host_port[0])

toks = ("/").join(toks[3:])
# print(toks)
if "?" in toks[0] and "#" in toks[0]:
   rest = toks[0].split("?")
   print("path: /" + rest[0])
   qs = rest[1].split("#")
   print("query-string: " + qs[0] + "\nfragment-id: " + qs[1])
elif "?" in toks[0]:
   rest = toks[0].split("?")
   print("path: /" + rest[0])
   print("query-string: " + rest[1])
elif "#" in toks[0]:
   rest = toks[0].split("#")
   print("path: /" + rest[0])
   print("fragment-id: " + rest[1])
else:
   print("path: /" + toks[0])
