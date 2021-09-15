# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

for _ in range(int(input())):

    f = int(input())
    s = []
    for i in range(f): s.append(list(map(int, input().rstrip().split()))) 
    # taking 2d array input

    container_rowsum = [0]*f 
    ball_type_colsum = [0]*f


    for i in range(f):
        for j in range(f):
            container_rowsum [i] = container_rowsum [i] + s[i][j]
            ball_type_colsum [j] = ball_type_colsum [j] + s[i][j]
    
    container_rowsum.sort()
    ball_type_colsum.sort()

    if container_rowsum == ball_type_colsum : print('Possible')
    else : print('Impossible')

'''
    Swaps that happen between any 2 buckets are always of equal value 
    (you can exchange 1 for 1 but not 2 for 1, ratio should always be 1:1), 
    therefore the number of balls in each bucket will always remain the same

    Calculate the number of balls in each container(sum of rows) and store it in a list
    Calculate the number of balls of each type(sum of columns) and store it in a list
    Sort the two lists and compare them. If they are equal then a solution exists otherwise, no solution exists.

    0 4 0 --> 4
    1 0 2 --> 3
    2 0 1 --> 3
    | | |
    3 4 3
    Column: 4, 3, 3 Row: 3, 4, 3
    A solution exists for this scenario but the column and row array don't match. 
    If we sort it, then, both arrays look similar: [3, 3, 4]. Hence we sort.
'''
