#!/usr/bin/env python3

from aux import *
import sys

"""
x = number to check
n = check for possible ways to write x with sum of n parts

[x-n+1, 1, 1, 1...]
length n -> sum is x

bsp fuer x = 6, n = 3

erster lauf: p = 4
4 1 1
3 1 2
2 1 3
1 1 4
zweiter lauf: p = 3
3 2 1
2 2 2
1 2 3 ! 123 == 321 lauf aufgabenstellung
dritter lauf: p = 2
2 3 ...

bsp fuer x=7, n=3
5 1 1
4 2 1
- 4 1 2
3 3 1
- 2 3 2 - 2 3 1
3 2 2
- 2 3 2 - 2 2 3


bsp fuer x=6, n=3
4 1 1
3 2 1
2 2 2
"""

VERBOSE = False

def check_if_summands_are_legit(summands):
    if VERBOSE:
        print(f"checking if {summands} are legit")
    for i in range(len(summands) - 1):
        if summands[i] < summands[i+1]:
            if VERBOSE:
                print("  no")
            return False 
    if VERBOSE:
        print("  yes")
    return True

def get_alternative_sums(summands):
    l = len(summands)
    count = 0
    for i in range(l-1):
        new_summands = summands[:]
        new_summands[0] -= 1
        new_summands[i+1] += 1
        if check_if_summands_are_legit(new_summands):
            # print(new_summands)
            count += 1
            count += get_alternative_sums(new_summands)
    return count 


def get_ways(number, amt_sums):
    summands = [1] * (amt_sums)
    summands[0] = number - amt_sums + 1
    # [number-n+1, 1, 1...]

    # print(summands)
    return get_alternative_sums(summands) + 1

NUMBER_TO_CHECK = int(sys.argv[1])
results = []
for j in range(1, NUMBER_TO_CHECK + 1):
    count = 0
    # print(f"checking the {j}")
    for i in range(2, j + 1):
        tmp = get_ways(j, i)
        count += tmp
    # print(f"  has {count} possible sums")
    results.append(count)
    # print(results)
    # print("")
    # print(f"Total combinations: {count}")
    # sys.stdout.write(str(count))

# print(results)

for i in range(len(results)):
    if i == 0:
        continue

    print(f"{i+1}\t{results[i]}\t{results[i] - results[i-1]}")
"""
22 0.6
23 1.6
24 4.8
25 11.2
"""