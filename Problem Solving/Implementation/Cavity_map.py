# https://www.hackerrank.com/challenges/cavity-map/problem

# the conditions are:
# 1) is right or left of the current value a value that is greater or equals
# 2) is above or below of the current value a value that is greater or equals
# 3) is it in the first or last row or is it the first or last number
# if so it cant be a cavity

# Conditions: right,left,top,down < center

#   0 1 2 3

#   1 1 1 2   0
#   1 9 1 2   1
#   1 8 9 2   2
#   1 2 3 4   3

n = int(input())
a = []
for _ in range(n):                                  # we are taking input here which will be string
    a.append(input())                               # we can take number but using string indexing can be done

print(a[0])                                         # first row can never have trench print it as it is

for i in range (1,n-1):                             # rows we will check from 2nd to 2nd last as both 1st and last can never have trench
    ans = a[i][0]                                   # initializing string with first column since corner values can never be trench

    for j in range (1,n-1):                         # columns also check from 2nd to 2nd last

        if int(a[i-1][j]) < int(a[i][j]) and \
            int(a[i+1][j]) < int(a[i][j]) and \
            int(a[i][j-1]) < int(a[i][j]) and \
            int(a[i][j+1]) < int(a[i][j]) :         # these all are the conditons which should satisfy to be a trench

            ans = ans + 'X'                         # add X to ans if trench

        else :
            ans = ans + a[i][j]                     # else value will be printed

    ans = ans + a[i][-1]                            # last value of column will never be trench and not tested in loop so adding it also
    print(ans)                                      # printing ans which will be complete row with X and numbers

if n != 1 : print(a[-1])                            # this prints last row as it will not be checked 
                                                    # will not be printed for n = 1 as a[0] we are printing in start so no need to reprint

