# https://www.hackerrank.com/challenges/closest-number/problem

import math

for _ in range(int(input())):    
    
    # input
    a, b, x = map(int, input().split())
    
    # find out a**b using math.pow (logn)
    # m * x = a**b --> this is the equation 
    # so just find m now and also 2 values of m*x with ceil and floor
    powab = math.pow(a, b)
    m = powab / x
    a1 = x * math.ceil(m)
    a2 = x * math.floor(m)
    
    # now we just need to find which value is close to a**b
    if abs(a2 - powab) < abs(a1 - powab):
        print(a2)
    else:
        print(a1)
    
