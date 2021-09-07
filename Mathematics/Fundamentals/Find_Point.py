# https://www.hackerrank.com/challenges/find-point/leaderboard

n = int(input())
for i in range(n) :
    p1, p2, q1, q2 = map(int, input().split())
    print(2*q1 - p1, 2*q2 - p2)
