# https://www.hackerrank.com/challenges/matrix-tracing/submissions/code/233052219
# https://www.hackerrank.com/challenges/matrix-tracing/editorial

import math

for _ in range(int(input())):
    n,m = map(int, input().split())
    paths = math.factorial(n-1+m-1) // (math.factorial(n-1)*math.factorial(m-1))
    print(paths % 1000000007)
    
# this sol gives TLE for some cases
''' The answer is that we have (N-1+M-1)!/((N-1)!(M-1)!) different paths for given M and N. 
For example for the sample input, we have (2-1+3-1)!/((2-1)!(3-1)!) = 3!/(1*2) which is 6/2= 3.
This is because there will be M-1 moves RIGHT and N-1 moves DOWN.

(m+n-2)(C)(m-1). 

Therefore for your example we can have (for 3x3)
RIGHT DOWN RIGHT
RIGHT RIGHT DOWN
DOWN RIGHT RIGHT

So these are just the permutations of M-1 RIGHT and N-1 DOWN '''
