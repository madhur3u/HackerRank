# https://www.hackerrank.com/challenges/sherlock-and-permutations/problem

# We fix a 1 at the first position. Now we are left with M-1 1s and N 0s. Now we can just count unique permutations 
# of (M-1) 1s and N 0s, which is choose((M+N-1), N), which is (M+N-1)!/(N! * (M-1)!)

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

# ex : for n = 2 means two 0, and m = 3 means 3 ones , 00111
# now we will fix one 1 at 1st position so it is 1 _ _ _ _
# we have 4 black poistion and need to find all permutations of remaining 0 and 1 which will be answer
# all permutations = 4! , but since there are two zeroes so divide by 2! to avoid repititions, same for 1 also
# therefore ans becomes --> 4! / (2! * 2!)
