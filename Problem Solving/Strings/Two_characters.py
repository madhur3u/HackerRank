# https://www.hackerrank.com/challenges/two-characters/problem
# https://studyalgorithms.com/string/hackerrank-two-characters/

# not at all an easy problem see above link and video for better explanantion
# DP

# func to print 2d array, not needed in q but made for debugging
def print2d(a, n):

    for i in range(n):
        for j in range(n):
            print(a[i][j], end='\t')
        print()

# n = int(input())
# s = input()

n = 10
s = 'beabeefeab'

# first take all distinct elements in string in a list
dist = sorted(set(s))
# print(dist)   # --> ['a', 'b', 'e', 'f']

# now make a 2d matrix (empty) with len(distinct el) as row and col
matrix = [["" for _ in range(len(dist))] for _ in range(len(dist))]
# print2d(matrix, len(dist))


# now starts our main loops
# take out the value in s one by one
# and also the index (j) at which that value lie in diatinct el array 
for value in s:
    j = dist.index(value)

    # add value to all rows if not X in that place 
    for i in range(len(dist)):

        if matrix[i][j] != 'X':		# check if not X (never at starting)

            matrix[i][j] += value
            if len(matrix[i][j]) >= 2 and matrix[i][j][-1] == matrix[i][j][-2] : 	# if two adjacent elements equal then cant be valid 
                matrix[i][j] = 'X'													# then make that el X, now we will not consider this
    
    # add values to all columns, same as rows
    for i in range(len(dist)):

        if matrix[j][i] != 'X':

            matrix[j][i] += value
            if len(matrix[j][i]) >= 2 and matrix[j][i][-1] == matrix[j][i][-2] :
                matrix[j][i] = 'X'
    
    # print2d(matrix, len(dist))

# print2d(matrix, len(dist))

# after coming out of the loop we will have either X as element of 2D matrix
# or we will have a string with only 2 el alternate
# now we will find length of max such string and we print that
# if max value is 1 means we never have a valid ans so print 0  
ans = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):

        ans = max (ans, len(matrix[i][j]))

print(ans if ans > 1 else 0)
