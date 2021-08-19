# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def reverse(n):
	x = str(n)
	x = x[::-1]
	return int(x)

def isPallindrome(n):
	x = str(n)
	return x == x[::-1]

def isLycherel(n):
	c = 0
	while(c<30):
		n = n + reverse(n)
		c += 1
		if isPallindrome(n): return False
	return True

def nthlychrelnumbers(n):
	# your code goes here
	c = 0
	x = 11
	while(c < n):
		if isLycherel(x):
			c += 1
		x += 1
	return x-1
