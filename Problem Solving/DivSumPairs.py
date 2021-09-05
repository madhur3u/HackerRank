# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

n, k = list(map(int, input().rstrip().split()))
a = list(map(int, input().rstrip().split()))
c = 0
for i in range (n) :
    for j in range (n-i-1) :
        s = a[i] +  a[i+j+1]
        if s % k == 0 : c = c + 1
        s = 0
print(c)
