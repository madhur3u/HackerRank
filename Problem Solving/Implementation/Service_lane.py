# https://www.hackerrank.com/challenges/service-lane/problem

n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    i1, i2 = map(int, input().split())
    print(min(a[i1:i2+1]))              # the max width of car will be the min of all lanes between given indices
