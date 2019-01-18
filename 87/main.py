#!/usr/bin/env python3

from aux import *
import math

primes = []
CEILING = 50000000
for i in range(1, math.ceil(math.sqrt(CEILING))):
	if checkPrime(i):
		primes.append(i)
values = set()
for p1 in primes:
	p1_2 = p1**2
	if p1_2 > CEILING:
		continue
	for p2 in primes:
		p2_3 = p2**3
		if p1_2 + p2_3 > CEILING:
			continue
		for p3 in primes:
			number = p1_2 + p2_3 + p3**4
			if number < CEILING:
				values.add(number)
print(len(values))
