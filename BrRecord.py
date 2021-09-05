# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

n = int(input())
a = list(map(int, input().rstrip().split()))
max1 = a[0]
min1 = a[0]
a.pop(0)
x = 0
y = 0
for i in a :
    if (i > max1) :
        x = x + 1
        max1 = i
    if (i < min1) :
        y = y + 1
        min1 = i

print(x,y) 
