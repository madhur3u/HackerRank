r, c , time = map(int, input().split())
grid1 = [input() for i in range(r)]

n = (time - 3) / 4
m = (time - 5) / 4


if time == 1 :
    for i in range(r):
        print(grid1[i])


elif time % 2 == 0 :
    for i in range(r):
        print('O'*c)


elif n % 1 == 0  :
    grid2 = [['O' for i in range(c)] for i in range(r)]
    grid3 =''

    for i in range(r):
        for j in range(c):

            if grid1[i][j] == 'O':
                
                grid2[i][j] = '.'
                if (i+1 < r) : grid2[i+1][j] = '.'
                if (i-1 >= 0) : grid2[i-1][j] = '.'
                if (j+1 < c) : grid2[i][j+1] = '.'
                if (j-1 >= 0) : grid2[i][j-1] = '.'
        
    for i in range(r):
        grid3 = grid3 + ''.join(grid2[i]) +'\n'

    print(grid3)


elif m % 1 == 0  :
    grid2 = [['O' for i in range(c)] for i in range(r)]
    grid3 =''

    for i in range(r):
        for j in range(c):

            if grid1[i][j] == 'O':
                
                grid2[i][j] = '.'
                if (i+1 < r) : grid2[i+1][j] = '.'
                if (i-1 >= 0) : grid2[i-1][j] = '.'
                if (j+1 < c) : grid2[i][j+1] = '.'
                if (j-1 >= 0) : grid2[i][j-1] = '.'
        
    
    grid4 = [['O' for i in range(c)] for i in range(r)]
    grid5 =''

    for i in range(r):
        for j in range(c):

            if grid2[i][j] == 'O':
                
                grid4[i][j] = '.'
                if (i+1 < r) :  grid4[i+1][j] = '.'
                if (i-1 >= 0) : grid4[i-1][j] = '.'
                if (j+1 < c) :  grid4[i][j+1] = '.'
                if (j-1 >= 0) : grid4[i][j-1] = '.'
        
    for i in range(r):
        grid5 = grid5 + ''.join(grid4[i]) +'\n'

    print(grid5)


