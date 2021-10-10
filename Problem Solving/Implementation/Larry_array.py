# https://www.hackerrank.com/challenges/larrys-array/problem

def count_Inversions(a, n):                     # bruteforce method to find inversions
    
    c = 0
    for i in range(n - 1):                      # compare a value with all other value to its right
        for j in range(i + 1, n):               # if we found a smaller no. than a[i] increase count

            if a[i] > a[j] :
                c += 1
    
    # print(c)
    return c


# main
for _ in range(int(input())):

    n = int(input())        
    arr = list(map(int, input().split()))       # input array

    inv = count_Inversions(arr, n)              # finding no. of inversions in array

    if inv % 2 == 0 : print('YES')              # if even inversions, sort is possible
    else            : print('NO')               # else NO

'''
An inversion occurs when the a given value in an array precedes another value in the array.
For this problem, the array can be solved with the given formula if the total number of inversions is even/divisible by 2.

A "rotation" does not change the parity of the number of inversions. That's the key to solving this. 
The array can be sorted only if the initial number of inversions is even (this is because you want 0 inversions at the end, which is even).

'''
# in order to check if the array can ever be sorted by rotating R consecutive elements until it gets sorted, 
# then the number of inversions should be divisible by R-1.
