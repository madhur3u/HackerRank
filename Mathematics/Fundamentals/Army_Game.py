# https://www.hackerrank.com/challenges/game-with-cells/problem

import math

n, m = map(int, input().split())

mn = min(n,m)
mx = max(n,m)

a = ((mx-mx//2)*(mx-mx//2))
if mx%2 == 0 : 
    b = mx - mx//2
    d = 1 + (mx-mn)//2
else : 
    b = -1 + mx - mx//2
    d = (1+mx-mn)//2

mul = b - d + 1
sq = int(math.sqrt(a))
print(sq*mul)
