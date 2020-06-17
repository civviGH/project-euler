#!/usr/bin/env python3
# https://projecteuler.net/problem=145

from aux import *
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
    r = reverse_number_2(n)
    return consists_of_odd_digits(n + r)

count = 0

for i in range(1,10**9):
    if (is_reversable(i)):
        count += 1
        # print(f"{i}\t{reverse_number(i)}\t{i+reverse_number(i)}")

print()
print(f"found {count} reversable numbers")
