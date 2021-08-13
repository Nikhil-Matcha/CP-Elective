# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	if row<0: return 0
	if col<0 or col>row: return 0
	pascal = []
	for i in range(row+1):
		currRow = []
		currRow.append(1)
		if i>=1:
			prevRow = pascal[i-1]
			for j in range(1, len(prevRow)):
				val = prevRow[j-1] + prevRow[j]
				currRow.append(val)
			currRow.append(1)
		pascal.append(currRow)
	return pascal[row][col]