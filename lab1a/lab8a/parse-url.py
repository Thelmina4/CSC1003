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
print(url)
s = input()
toks = s.split(":")
print(toks)
