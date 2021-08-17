# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	num = str(n)
	c = [num.count(str(i)) for i in range(10)]
	res = 0
	for i in range(len(c)):
		if c[i]>c[res]:
			res = i
	return res