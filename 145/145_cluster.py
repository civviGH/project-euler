#!/usr/bin/env python3
# https://projecteuler.net/problem=145

import sys

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
FROM = int(sys.argv[1])
TO = int(sys.argv[2])

for i in range(FROM,TO):
    if (is_reversable(i)):
        count += 1
        # print(f"{i}\t{reverse_number(i)}\t{i+reverse_number(i)}")

print(count)
