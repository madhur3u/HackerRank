# https://www.hackerrank.com/challenges/kangaroo/problem

arr = list(map(int, input().rstrip().split()))
x1,v1,x2,v2 = arr
a = True
if (x1 == x2) : 
    print('YES')
    exit(0)
if (v2 > v1 or v2 == v1) :
    print('NO')
    exit(0)
while a :
    x1 = x1 + v1
    x2 = x2 + v2
    if x1>x2 and v1>v2 :
        print('NO')
        break
    if x1 == x2 :
        print('YES')
        break
