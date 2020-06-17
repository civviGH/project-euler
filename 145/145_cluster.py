#!/usr/bin/env python3
# https://projecteuler.net/problem=145

import sys
import os
import math

def consists_of_odd_digits(n):
    for digit in map(int, str(n)):
        if digit % 2 == 0:
            return False
    return True

def reverse_number(n):
    return int(str(n)[::-1])

def is_reversable(n):
    if str(n)[-1] == '0':
        return False
    r = reverse_number(n)
    return consists_of_odd_digits(n + r)

count = 0
# SLURM_PROCID ranges from 0 to NTASKS
LIMIT = int(sys.argv[1])
d_s = math.ceil(LIMIT/int(os.getenv("SLURM_NTASKS")))
FROM = 1 + int(os.getenv("SLURM_PROCID")) * d_s
TO = FROM + d_s

for i in range(FROM,TO):
    if (is_reversable(i)):
        count += 1
        # print(f"{i}\t{reverse_number(i)}\t{i+reverse_number(i)}")
print(count)
