#!/usr/bin/env python3

import math
import os
import sys

def factorial_chain(n):
    s = 0
    for d in map(int, str(n)):
        s += math.factorial(d)
    return s

def chain_length(n):
    visited = [n]
    while True:
        next_number = factorial_chain(visited[-1])
        if next_number in visited:
            break
        visited.append(next_number)
    return len(visited)

LIMIT = int(sys.argv[1])
d_s = math.ceil(LIMIT/int(os.getenv("SLURM_NTASKS")))
FROM = 1 + int(os.getenv("SLURM_PROCID")) * d_s
TO = min(FROM + d_s, LIMIT)

c = 0
for i in range(FROM,TO):
    if (chain_length(i) == 60):
        c += 1

print(c)
