import math

def generatePrimes(n1, n2):
  primes = []
  for i in range(n1, n2+1):
    if checkPrime(i):	
      primes.append(i)
  return primes	

def checkPrime(number):
  if number <= 1:
    return False
  if number == 2:
    return True
  if number%2 == 0:
    return False
  for i in range(3, int(math.ceil(math.sqrt(number)+1)), 2):
    if number%i == 0:
      return False
  return True

def checkPerm(n1, n2):
  s1 = str(n1)
  s2 = str(n2)
  if len(s1) != len(s2):
    return False
  if sorted(s1) == sorted(s2):
    return True
  return False
