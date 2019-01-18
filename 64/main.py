#!/usr/bin/env python3

from aux import *
import math
from fractions import Fraction

number = 23
start = math.sqrt(number)

s = ""
PRECISION = 10000
ganz = int(start)
#rest = Fraction(start - ganz).limit_denominator(PRECISION)
rest = Fraction(start - ganz)
for i in range(100):
	try:
		right = (1/rest)
	except:
		print("rip")
		break
	ganz = int(right)
	if ganz > number:
		print("rip2")
		break
	s = s + str(ganz)
	rest = right - ganz
print(s)
