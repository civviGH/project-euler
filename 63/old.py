#!/usr/bin/env python3

from aux import *

exponent = 1
hits = 0
while True:
    s = 0
    base = 1
    while s <= exponent:
        num = base**exponent
        s = len(str(num))
        if (s == exponent):
            hits += 1
            print(f"Hit: {base}^{exponent} = {num}\t{hits}")
        base += 1
    exponent += 1

# base = 1
# hits = 0
# while base < 10:
#     print(f"Starting with base: {base}")
#     s = 1
#     exponent = 1
#     while s >= exponent:
#         num = base**exponent
#         print(f"  {base}^{exponent} = {num}")
#         s = len(str(num))
#         if (s == exponent):
#             hits += 1
#             # print(f"Hit: {base}^{exponent} = {num}\t{hits}")
#         exponent += 1
#     base += 1