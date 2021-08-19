# makeMagicSquare(n)
# Write the function makeMagicSquare(n) that takes a positive 
# odd integer n and returns an nxn magic square by following 
# the resource here. If n is not a positive odd integer, 
# return None.

# URL: https://en.wikipedia.org/wiki/Magic_square

# Hints: From Geeks for Geeks.
# Did you find any pattern in which the numbers are stored? 

# In any magic square, the first number i.e. 1 is 
# stored at position (n/2, n-1). Let this position 
# be (i,j). The next number is stored at position (i-1, j+1) 
# where we can consider each row & column as circular array 
# i.e. they wrap around.

# Three conditions hold:

# 1. The position of next number is calculated by 
# decrementing row number of the previous number by 1,
#  and incrementing the column number of the previous 
# number by 1. At any time, if the calculated row position 
# becomes -1, it will wrap around to n-1. Similarly, if 
# the calculated column position becomes n, it will wrap 
# around to 0.

# 2. If the magic square already contains a number at the 
# calculated position, calculated column position will be 
# decremented by 2, and calculated row position will be 
# incremented by 1.

# 3. If the calculated row position is -1 & calculated 
# column position is n, the new position would be: (0, n-2). 

def makeMagicSquare(n):
    # Your code goes here...
    if n<0 or n%2==0:
        return None
    res = [[0 for i in range(n)] for j in range(n)]
    x = n//2
    y = n-1
    for i in range(1, n*n + 1):
        if x == -1 and y == n:
            x = 0
            y = n-2
        elif x == -1:
            x = n-1
        elif y == n:
            y = 0
        elif res[x][y] != 0:
            x = x+1
            y = y-2
        res[x][y] = i
        x = x-1
        y = y+1
    return res

print(makeMagicSquare(5))