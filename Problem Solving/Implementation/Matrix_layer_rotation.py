# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

# matrix shell rotation all layers
# there will always be a shell as min(n,m)%2 = 0 is a constrain
# logic is to take each shell --> make a 1d array of it --> rotate that 1D array --> fill it again in 2D array
# no. of shells --> min(n,m) // 2 

# to rotate whole matrix we do 3 things for each shell
# 1. take out the shell as 1d array using border approach of matrix traversal
# 2. rotate that 1d array obtained by r
# 3. now update the shell of 2d array by the rotated 1d array
# this function calls 3 function which do these 3 tasks    
def rotateShell(arr, shell, n, m, r):

    a = make1Darray(arr, shell, n, m)
    a = rotate1Darray(a, r)
    update2darray(arr, a, shell, n, m)

# in this we make 1d array of the shell 
# same as ring rotate and return that 1d array
def make1Darray(arr, shell, n, m):

    rmin = shell - 1
    cmin = shell - 1
    rmax = n - shell
    cmax = m - shell

    a1 = []
    i = rmin
    j = cmin

    for _ in range(rmax - rmin):
        a1.append(arr[i][j])
        i+=1
    
    for _ in range(cmax - cmin):
        a1.append(arr[i][j])
        j+=1

    for _ in range(rmax - rmin):
        a1.append(arr[i][j])
        i-=1

    for _ in range(cmax - cmin):
        a1.append(arr[i][j])
        j-=1

    # print(*a1)
    return a1

# in this we rotate our 1d array and return it
def rotate1Darray(a, r):

    n = len(a)
    r = r % n
    if r == 0 : return a		# if r = 0 no need to rotate

    a = a[n - r - 1 : : -1] + a[ : n - r - 1 : -1] 
    a = a[ :: -1]
    
    return a

# in this we update our shell with the rotated 1d array in same matrix
def update2darray(arr, a1, shell, n, m):

    rmin = shell - 1
    cmin = shell - 1
    rmax = n - shell
    cmax = m - shell

    i = rmin
    j = cmin

    a1Index = 0

    for _ in range(rmax - rmin):
        arr[i][j] = a1[a1Index]
        a1Index += 1
        i+=1

    
    for _ in range(cmax - cmin):
        arr[i][j] = a1[a1Index]
        a1Index += 1
        j+=1

    for _ in range(rmax - rmin):
        arr[i][j] = a1[a1Index]
        a1Index += 1
        i-=1

    for _ in range(cmax - cmin):
        arr[i][j] = a1[a1Index]
        a1Index += 1
        j-=1

    # print(*a1)
    return a1
    
# main 
n, m, r = map(int, input().split())							# input of row len, col len and no. of rotations
matrix = [list(map(int, input().split())) for i in range(n)]	# input 2D array

for shell in range(1, min(n,m)//2 + 1):							# this loop give us no. of shells, no of shells always min(n,m)//2
    rotateShell(matrix, shell, n, m, r)							# rotating each shell of matrix

for i in range(n):									# printing rotated matrix
    print(*matrix[i])
