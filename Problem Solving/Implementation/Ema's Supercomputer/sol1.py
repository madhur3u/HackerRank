# https://www.hackerrank.com/challenges/two-pluses/problem


input_grid = []
n, m = map(int, input().split())
for _ in range(n):
    input_grid.append(input())                              # taking input of grid which will be as string for rows

# print(grid)
grid = []                                                   # making string grid into a 2D array
for i in range (n + 2):                                     # this 2D array will have a border of 'O' around it to ensure index out of range error is handled
        
    if i == 0 or i == n + 1 :                               # 1st and Last row will only have 'O' 
        grid.append(['O' for _ in range(n + 2)]) 
        
    else :                                                  # from 2nd to 2nd last row of our 2D array
        row_grid = ['O']                                    # border, j==0 will have 'O'
        for j in range(m):                                  
            row_grid.append(input_grid[i-1][j])             # middle elements are initialized using the input_grid
        
        row_grid.append('O')                                # border, last column will be 'O'

        grid.append(row_grid)                               # push this list of row into grid

    # print(*grid[i])

# iterate from row 2 till 2nd last row and find 2 plus , store their area multiplied somewhere
# now when we go to next row, we do it again and if area is greater this time, take this area and so on

# ! 1st plus we will find depending on rows, for second plus we find maximum possible plus which we can find after 1st plus found

# our logic is to find 1st plus, convert all G there into some other element (.) to avoid repititions
# then find out 2nd plus, we have already handled repitions so we will get next maximum plus which can be formed around that row

area = 0

# iteration for first plus 
for i in range(1, n + 1):
    for j in range(1, m + 1):

        r = 0                                               # r will track the 1st plus length
        while   grid [i][j - r] == 'G' and \
                grid [i][j + r] == 'G' and \
                grid [i - r][j] == 'G' and \
                grid [i + r][j] == 'G' :

            grid [i][j - r] =  grid [i][j + r] = grid [i - r][j] = grid [i + r][j] = '.'    # if found a G, replace it with '.' to avoid repeat

            
            # iteration for second plus
            for I in range(1, n + 1):
                for J in range(1, m + 1):

                    R = 0                                   # R will track the 2nd plus length 
                    while   grid [I][J - R] == 'G' and \
                            grid [I][J + R] == 'G' and \
                            grid [I - R][J] == 'G' and \
                            grid [I + R][J] == 'G' :

                        area = max (area, (4*r + 1)*(4*R + 1))          # if we find plus the area of 1st plus (4*r + 1) multilpy by 2nd (4*R + 1)
                        R = R + 1                                       # R inc to check biiger 2nd plus if exist for a constant 1st plus length
            
            r = r + 1                                       # now increase 1st plus length, and for this length find all 2nd plus that exist, find area
        # print('_______________')                          # DEBUGGING
        # for P in range(n+2) : print(*grid[P])
        r = 0                                               # now r = 0 for next value of j
        while   grid [i][j - r] == '.' and \
                grid [i][j + r] == '.' and \
                grid [i - r][j] == '.' and \
                grid [i + r][j] == '.' :                    # revert back the grid to original

            grid [i][j - r] =  grid [i][j + r] = grid [i - r][j] = grid [i + r][j] = 'G'
            r = r + 1

print(area)                     # area will have the answer 
