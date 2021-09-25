# https://www.hackerrank.com/challenges/bomber-man/problem
# https://www.hackerrank.com/challenges/bomber-man/editorial


def UPDATE_GRID(G) :
    new_grid = [['O' for i in range(c)] for j in range(r)]  # new grid formed using all O, means all bombs

    for i in range(r) :
        for j in range(c) :
            if ((G[i][j]=='O') or 
                (j+1< c and G[i][j+1]=='O') or 
                (j-1>=0 and G[i][j-1]=='O') or 
                (i-1>=0 and G[i-1][j]=='O') or 
                (i+1< r and G[i+1][j]=='O')) :      # we check in if block the input grid position of bombs and according to that update new grid
                
                new_grid[i][j] = '.'
    
    return new_grid

###################################################################

def printGrid(grid) :                               # print grid function print the grid in required format
    for row in grid :
        print("".join(row))

###################################################################

# main 
r, c, time = map(int, input().split())              # taking inputs
input_grid = [input() for _ in range(r)]            # input array

if time % 2 == 0 :                                  # if time is odd all bombs
    printGrid([['O']*c for i in range(r)])

else :                                              # case for odd time
    if time == 1 :                                  # if time is 1 then grid is same as input
        printGrid(input_grid)
        
    elif time % 4 == 3 :                             
        printGrid(UPDATE_GRID(input_grid))

    else :
        printGrid(UPDATE_GRID(UPDATE_GRID(input_grid)))

###################################################################

'''
FOR EVEN TIME :  
    If 'time' is even, then we can get the answer very easily, without simulation. 
    Notice that new bombs are only planted after even seconds have passed (including zero), and bombs only detonate after odd seconds have passed. 
    This means that if 'time' is even, then after 'time'seconds the whole grid will be filled with bombs. 
    Thus, we only need to handle the case where 'time' is odd. 

FOR TIME == 1 :
    For time = 1 the pattern will be same as what INPUT is as, no bomb is detonating and no new bomb is added

FOR TIME == 3 : time % 4 == 3 :
    In this time all bombs planted initially will blast and will take bombs in adjacent cells also which was placed at even time.
    So we make a new grid 1st with all places filled with bomb.
    Now we traverse through INPUT_GRID and update which all places will be empty after INPUT_GRID bomb detonates.

    if ((G[i][j]=='O') or 
        (j+1< c and G[i][j+1]=='O') or 
        (j-1>=0 and G[i][j-1]=='O') or 
        (i-1>=0 and G[i-1][j]=='O') or 
        (i+1< r and G[i+1][j]=='O')) : 
                    
        X[i][j] = '.'

    cases at corners of grid are also taken in consideration by checking values of i and j 

FOR TIME == 5 : or for all odd cases other than time % 4 == 3 :
    At this time the bomb planted at TIME 2 will detonate, bomb planted at TIME 2 are shown by the GRID we got in TIME 3.
    At time 4 all places will be filled by bombs again and, at timr 5 all bombs which were in TIME 3 will detonates.
    So we consider GRID of TIME 3 as INPUT_GRID and get our answer

    printGrid(UPDATE_GRID(UPDATE_GRID(input_grid)))

    thats why we call fn 2 times, 1st time it make GRID3 and after that GRID5, using GRID3 as INPUT_GRID


After time 5 the grid will repeat
time
1
2   6   10  14
3   7   11  15      for all these values we need to print GRID3
4   8   12  16
5   9   13  17      for all these values we need to print GRID5

the pattern will repeat like this sequence it will be diff for 1 and after that for consecutive odds it will repeat.
even already taken care of

Grid 3 is already found
Grid 5 is already found

so we make a formula    time % 4 == 3   , this will take care of all grids 3,7,11,15... where we need to change GRID only once

in the else block       5,9,13,17... will be taken care of where we need to change GRID twice
'''
