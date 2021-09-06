# https://www.hackerrank.com/challenges/sock-merchant/problem 

n = int(input())
a = list(map(int, input().split()))
a.sort()
i = 0
c = 0
while i < n - 1 :
    if a[i] == a[i+1] :
        i = i + 2
        c = c + 1
    else : i = i + 1
print(c)
