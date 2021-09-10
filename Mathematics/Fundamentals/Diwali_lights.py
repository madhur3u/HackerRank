# https://www.hackerrank.com/challenges/diwali-lights/problem

q = int(input())
for x in range(q):
    n = int(input())
    
    sum1 = 2**n - 1 # sum of all combinations of n
    print(sum1 % 100000)

# for java BITINTEGER to be used in this q    
