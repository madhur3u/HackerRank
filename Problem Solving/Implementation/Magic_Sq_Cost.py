# https://www.hackerrank.com/challenges/magic-square-forming/problem
# HARD

s = []
for i in range(3):
    s.append(list(map(int, input().split())))

s1 = sum(s, [])
magic =     [
            [8, 1, 6, 3, 5, 7 ,4, 9, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 9, 4, 7, 5, 3 ,6, 1, 8], 
            [8, 3, 4, 1, 5, 9 ,6, 7, 2],
            [4, 3, 8, 9, 5, 1 ,2, 7, 6], 
            [6, 7, 2, 1, 5, 9, 8, 3, 4], 
            [2, 7, 6, 9, 5, 1, 4, 3, 8],
            ] # here we have taken all magic squares which are possible for 3x3 then we subtract given list(conv to 1d) from each magic square
              # and then we will take minimum of all 9 answers we get in minc 

minc = 45
for mag in magic :
    d = 0
    for i,j in zip(s1, mag): #if we have 2 1d lists s1 and mag both equal we can use zip, it will give 1st value of s1 to i and 1st value of mag to j
        d = d + abs(i-j)
    minc = min(minc, d)

print(minc)
