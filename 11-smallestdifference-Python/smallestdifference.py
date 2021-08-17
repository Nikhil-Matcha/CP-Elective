# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	if len(a)==0:
		return -1
	temp = sorted(a)
	res = 1000000
	for i in range(len(temp)-1):
		x = temp[i+1] - temp[i]
		if x < res:
			res = x
	return res