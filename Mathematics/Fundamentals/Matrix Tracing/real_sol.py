# https://www.hackerrank.com/challenges/matrix-tracing/problem

import math

def fact(n, p):
    prod = 1
    if (n >= p): return 0
    
    for i in range(1,n+1):
        prod = (prod * i)%p

    return prod

def solve(m, n):
    x = fact(m+n-2, 1000000007)
    y = pow(fact(m-1, 1000000007) * fact(n-1, 1000000007), 1000000005, 1000000007)
    return x*y%1000000007

T = int(input())
for i in range(0,T):
    nums = input()
    m, n = nums.split()
    m = int(m)
    n = int(n)
    print(solve(m, n))
    
''' The answer is that we have (N-1+M-1)!/((N-1)!(M-1)!) different paths for given M and N. 
For example for the sample input, we have (2-1+3-1)!/((2-1)!(3-1)!) = 3!/(1*2) which is 6/2= 3.
This is because there will be M-1 moves RIGHT and N-1 moves DOWN.
(m+n-2)(C)(m-1). 
Therefore for your example we can have (for 3x3)
RIGHT DOWN RIGHT
RIGHT RIGHT DOWN
DOWN RIGHT RIGHT
So these are just the permutations of M-1 RIGHT and N-1 DOWN '''
