# https://www.hackerrank.com/challenges/electronics-shop/problem

n  = int(input())
for i in range(n):
    x,y,z = list(map(int, input().split()))

    if (abs(x-z) == abs(y-z)) : print('Mouse C')
    elif (abs(x-z) > abs(y-z)) : print('Cat B')
    else : print('Cat A')
