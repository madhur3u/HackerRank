# https://www.hackerrank.com/challenges/strange-advertising/problem

n = int(input())

s = 5 #on day 1
l = 2 #on day 1
for i in range(n-1): # will run from day 2 onwards
    s = 3 * (s//2)
    l = l + s//2
print(l)
