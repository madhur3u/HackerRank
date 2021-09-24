# https://www.hackerrank.com/challenges/strange-code/problem
# O(1)

import math

s = int(input())                              # input number
n = math.log(s/3 + 1 ) / math.log(2)          # taking input number as sum of GP we find n, as a = 3, r = 2
# print(math.log(s/3 + 1 ) / math.log(2))

if n % 1 == 0 : print(1)                      # n will exactly be an integer if s is exact sum, so since value is decreasing so at s = exact sum answer is always 1

else :
    n = int(n)                                # taking floor of n for not exact integer
    Sn = 3 * (2**n - 1)                       # find out the sum of GP series till n,
    ans = (3*(2**n)) - (s - Sn) + 1           # 3*2**n is the nth element of GP
    print(ans)
    
    
# sum of gp, s = [a*(r**n - 1)] / (r-1)
# her we have, r = 2, a = 3
#             s = 3*(2**n - 1)
#             2**n = (s/3 + 1)
#             n = log(s/3 + 1) / log 2
 
'''    
t = int(input())  # alternate way using loop

t1 = 3
while(t1 < t):
    t -= t1
    t1 *= 2
    
print(t1 - t + 1)

'''
