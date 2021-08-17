# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.

def fun_kth_occurrences(s, n):
	count = dict()
	for c in s:
		if c not in count:
			count[c] = 1
		else:
			count[c] += 1
	x = sorted(count.values(), reverse=True)
	for key, value in count.items():
		if value == x[n-1]:
			return key
