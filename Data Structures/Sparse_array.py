# https://www.hackerrank.com/challenges/sparse-arrays/problem

n1 = int(input())
a =[]
for i in range(n1) : a.append(input())

n2 = int(input())
b =[]
for i in range(n2) : b.append(input())

for i in range(n2) :
    c = 0
    for j in range(n1) :
        if b[i] == a[j] : c += 1
    
    print(c)
