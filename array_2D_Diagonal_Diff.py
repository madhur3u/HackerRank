# diag diff of 2d array O(n)

n = int(input())
a = []
for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))
s1 = 0 
s2 = 0
for i in range(n):
    s1 = s1 + a[i][i] 
    s2 = s2 + a[i][n-i-1]
print(abs(s1-s2))
