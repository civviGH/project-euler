#!/usr/bin/env python3

from aux import *

def task49():
	primes = []
	for i in range(1000, 10000):
		if checkPrime(i):
			primes.append(i)
	for p1 in primes:
		for p2 in [i for i in primes if i > p1]:
			diff = p2 - p1
			if p2+diff in primes:
				if checkPerm(p1, p2):
					if checkPerm(p1, p2+diff):
						print("{}\t{}\t{}".format(p1, p2, p2+diff))

if __name__ == "__main__":
	task49()
