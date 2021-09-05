# https://www.hackerrank.com/challenges/kangaroo/problem

arr = list(map(int, input().rstrip().split()))
x1,v1,x2,v2 = arr
a = True
if (x1 == x2) : 
    print('YES')
    a = False
while a :
    x1 = x1 + v1
    x2 = x2 + v2
    if x1>x2 and v1>v2 :
        print('NO')
        break
    if x2>x1 and v2>v1 :
        print('NO')
        break
    if x2!=x1 and v2==v1 :
        print('NO')
        break
    if x1 == x2 :
        print('YES')
        break
