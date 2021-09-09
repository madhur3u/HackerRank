# https://www.hackerrank.com/challenges/reverse-game/problem

''' ALT BEST TIME SOLUTION
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k < n // 2:
        print(2 * k + 1)
    else:
        print(2 * (n - k - 1)) '''

n = int(input())
for i in range(n):
    n, k = map(int, input().split())
    a = []
    b = []
    for i in range(n): a.append(i)
    i = 0
    j = n-1
    for i in range(n//2):
        b.append(a[j])
        b.append(a[i])
        j-=1

    if n % 2 != 0 : b.append(a[j])
    print(b.index(k))

