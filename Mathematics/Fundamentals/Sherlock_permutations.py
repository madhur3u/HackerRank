# https://www.hackerrank.com/challenges/sherlock-and-permutations/problem

def fact(n) :
    f = 1
    for i in range(2,n+1): f = f*i
    return f

q = int(input())
for x in range(q):
    n, m = map(int, input().split())
    m = m-1
    x = fact(n+m)//(fact(n)*fact(m))  # no. of ways it can arrange unique is 1 * (n+m)! // (n! * m!) 
    print(x % 1000000007)
