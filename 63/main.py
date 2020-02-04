#!/usr/bin/env python3

from aux import *

base = 1
hits = 0
baselist = [0] * 9
print(baselist)
while base < 10:
    print(f"Starting with base: {base}")
    s = 1
    exponent = 0
    while s >= exponent:
        exponent += 1
        num = base**exponent
        print(f"  {base}^{exponent} = {num}")
        s = len(str(num))
        if (s == exponent):
            hits += 1
            baselist[base-1] += 1
            # print(f"Hit: {base}^{exponent} = {num}\t{hits}")
    print(f"Stopped because {s} < {exponent}")
    base += 1

for i in range(9):
    print(f"{i+1}\t{baselist[i]}")
# print(hits)