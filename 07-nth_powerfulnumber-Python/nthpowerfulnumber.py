# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math

def isPrime(n):
	if n<2: return False
	if n==2: return True
	for i in range(2, int(math.sqrt(n)+1)):
		if n%i==0: return False
	return True

def getPrimeFactors(n):
	res = []
	for i in range(2,n+1):
		if isPrime(i) and n%i==0:
			res.append(i)
	return res

def isPowerful(n):
	primeFactors = getPrimeFactors(n)
	for num in primeFactors:
		if n%(num*num)!=0:
			return False
	return True

def nthpowerfulnumber(n):
	# Your code goes here
	if n==0: return 1
	c = 0
	x = 2
	while(c<n):
		if isPowerful(x):
			c += 1
		x += 1
	return x-1
