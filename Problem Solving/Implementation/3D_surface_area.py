# https://www.hackerrank.com/challenges/3d-surface-area/problem

#     0   1   2

# 0   1   3   4

# 1   2   2   3

# 2   1   2   4


# finding the side_area according to rows let initial side_area be sum of 1st row
# side_area = 1 + 3 + 4 = 8
# now in side_area loop we will check from 2nd row and if an element is greater than the element of its previous row then we nee to add the
# extra area of how much greater it is -> side_area += (a[i][j] - a[i-1][j])

# finding the front_area according to columns let initial front_area be sum of 1st column
# front_area = 1 + 2 + 1 = 4
# now in front_area loop we will check from 2nd column and if an element is greater than the element of its previous column then we nee to add the
# extra area of how much greater it is -> front_area += (a[i][j] - a[i][j-1])

# now front and back area will be same and same for both left and right sides so we multiply these area by 2
# also top and bottom_area will always be H*W 

# therefore ans is -> front_area*2 + side_area*2 + bottom_area*2

H, W = list(map(int, input().split()))
a = []
front_area = 0                                  

for i in range(H):
    a.append(list(map(int, input().split())))       # 2D array input
    front_area += a[i][0]                           # front area as sum of 1st column

side_area = sum(a[0])                               # side area as sum of 1st row
bottom_area = H*W                                   # bottom area


for i in range(1,H):
    for j in range(W):
        if a[i][j] > a[i-1][j] : 
            side_area += (a[i][j] - a[i-1][j])      # side area loop

for j in range(1,W):
    for i in range(H):
        if a[i][j] > a[i][j-1] : 
            front_area += (a[i][j] - a[i][j-1])     # front area loop

print(front_area*2 + side_area*2 + bottom_area*2)
