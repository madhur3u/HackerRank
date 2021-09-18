# https://www.hackerrank.com/challenges/matrix-tracing/problem

import math
mod = 10**9 + 7

def modinv(n,p):
    return pow(n,p-2,p)

def ncr(n,r,p):
    if r > n:
        return 0
  
    nu = 1
    for i in range(n-r+1, n+1):
        nu = (nu * i) % p
  
    de = 1
    for i in range(2,r+1):
        de = (de * i) % p
    return (nu * modinv(de, p)) % p

for case in range(int(input())):
    (m,n) = map(int, input().split())
    print(ncr(m+n-2, n-1, mod))
    
''' The answer is that we have (N-1+M-1)!/((N-1)!(M-1)!) different paths for given M and N. 
For example for the sample input, we have (2-1+3-1)!/((2-1)!(3-1)!) = 3!/(1*2) which is 6/2= 3.
This is because there will be M-1 moves RIGHT and N-1 moves DOWN.
(m+n-2)(C)(m-1). 
Therefore for your example we can have (for 3x3)
RIGHT DOWN RIGHT
RIGHT RIGHT DOWN
DOWN RIGHT RIGHT
So these are just the permutations of M-1 RIGHT and N-1 DOWN '''
