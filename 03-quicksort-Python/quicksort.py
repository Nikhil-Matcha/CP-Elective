"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(low, high, array):
	pivot_index = low
	pivot = array[pivot_index]
	while low < high:
		while low < len(array) and array[low] <= pivot:
			low += 1
		while array[high] > pivot:
			high -= 1
		if low < high:
			array[low], array[high] = array[high], array[low]
	array[high], array[pivot_index] = array[pivot_index], array[high]
	return high

def quicksort1(low, high, array):
	if low < high:
		p = partition(low, high, array)
		quicksort1(low, p-1, array)
		quicksort1(p+1, high, array)

def quicksort(array):
	# Your code goes here
	low = 0
	high = len(array) - 1
	quicksort1(low, high, array)
	return array