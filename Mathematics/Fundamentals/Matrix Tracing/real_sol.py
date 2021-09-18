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
