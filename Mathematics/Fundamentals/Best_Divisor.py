# https://www.hackerrank.com/challenges/best-divisor/problem

def dsum(n):
    d = 0
    while(n != 0):
        d = d + n % 10
        n = n//10
    return d

n = int(input())
m = 0
y = 1
for i in range(n,1,-1):
    if (n % i == 0):
        x = dsum(i)
        if(x >= m) :
            m = x
            y = i

else : print(y)

