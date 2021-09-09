# https://www.hackerrank.com/challenges/utopian-tree/problem
# analyse the series and then see the GP formation

q = int(input())
for o in range(q):
    n = int (input())
    
    if n % 2 == 0 : 
        ans = 1 + 2*((2**(n//2) - 1))   # sum of GP
    else : 
        ans = 2*((2**(n//2 + 1) - 1))
    
    print(ans)
    
