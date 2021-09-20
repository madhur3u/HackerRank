# https://www.hackerrank.com/challenges/halloween-sale/problem

p,d,m,s = map(int, input().split())
sum = 0
c = 0

while p >= m :
    sum = sum + p
    if sum > s : break
    c+=1
    p = p - d

p = m
while True:
    sum = sum + p
    if sum > s : break
    c+=1

print(c)
