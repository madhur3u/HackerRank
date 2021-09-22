# https://www.hackerrank.com/challenges/best-divisor/problem

def dsum(n):                        # this will give us digit sum of number
    d = 0
    while(n != 0):
        d = d + n % 10
        n = n//10
    return d

n = int(input())
m = 0
y = 1

for i in range(n,1,-1):             # we need to find how any no follow the criteria so loop from n to 2 as 1 always a best divisor     
    
    if (n % i == 0):                # the number should be a divisor of n so checking that
        
        x = dsum(i)                 # this fn five us sum of digit of number
        
        if(x >= m) :                # in m we will store the sum of digit of previous number and 0 for 1st no.
            m = x                   # if x > m we will store in m new value
            y = i                   # y which will be our final answer will be given the value i which is present best divisor

print(y)

