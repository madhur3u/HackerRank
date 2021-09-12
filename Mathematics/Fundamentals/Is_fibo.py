# https://www.hackerrank.com/challenges/is-fibo/problem

a = 0
b = 1
fibo =[0]*50
for i in range(50):
    c = a + b
    fibo[i] = a
    a = b
    b = c

for _ in range(int(input())):
    n = int(input())
    if n in fibo : print('IsFibo')
    else : print('IsNotFibo')

# A number N is a Fibonacci number if 5*N2 ± 4 is a perfect square. Proof is given here On page 418.
# A smart way to check a number to be a perfect square is apply sqrt(N) % 1 == 0. 
''' alt solution

import math
for i in range(input()):
    n=input()
    r1 = sqrt(5*n**2+4)
    r2 = sqrt(5*n**2-4)

    if(r1%1 == 0 or r2%1==0):
        print "IsFibo"
    else:
        print "IsNotFibo"   '''
