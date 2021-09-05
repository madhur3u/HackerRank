# https://www.hackerrank.com/challenges/the-birthday-bar/problem

n = int(input())
a = list(map(int, input().rstrip().split()))
sum1, el = list(map(int, input().rstrip().split()))
c = 0
for i in range (n-el+1) :
    s = 0
    for j in range (el) :
        s = s +  a[i+j]
        
    if s == sum1 : c = c + 1 

print(c)
