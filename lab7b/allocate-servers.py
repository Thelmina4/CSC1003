#!/usr/bin/env python3

# brief = how many servers needed to service workload
#         workload = seq of jobs
#         each job = 1000ms to service (milliseconds)
#         1 server, 1 job at a time
#         more jobs at the same time = more servers
#         there must always be a server availabe

# s/i = seq of ints, how long a job is in ms
#       ordered by arrival time
#       terminated w "end"

work_finished = 1000

a = []
s = input()
while s != "end":
   a.append(int(s))
   s = input()

# print(job)
servers = []
count = 1
job_t = 1000
i = 1
j = 2
while len(a) != 0 and j < len(a):
   prev = a[i - 1]
   curr = a[i]
   next = a[j]
   if next - curr < 1000:
      count += 1
   elif 2 < len(a) and job_t < prev - curr and prev - next < job_t:
      servers.append(str(count))
      count = 0


   j += 1
   i += 1
print(i , j, len(a), servers)
