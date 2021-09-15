# https://www.hackerrank.com/challenges/jim-and-the-jokes/problem

# this will check if the no. is legal for the given base
def checkbase(d,m):
    while d!= 0:
        r = d % 10
        d = d / 10
        if r >= m : return 0
    return 1

# any base to decimal conversion
def decimalconv (d,m):
    if checkbase(d,m) == 0 : return 0
    s = 0
    p = 0
    while d != 0 :

        r = d % 10
        s = s + r * (m**p)
        p += 1
        d = d // 10

    return s

# main 
a = []
for _ in range(int(input())):

    m,d = map(int, input().split())
    a.append(decimalconv(d,m))

a.sort()
i = 0
x = 0
while i < len(a) - 1:
    n = 1
    if a[i] > 0:
        while a[i] == a[i + 1] : 
            n += 1
            i += 1
            if i == len(a)-1 : break
    i += 1
    x += (n*(n-1))//2

print(x)    
