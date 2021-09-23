# https://www.hackerrank.com/challenges/diwali-lights/problem

q = int(input())
for x in range(q):
    n = int(input())
    
    sum1 = 2**n - 1             # sum of all combinations of n
    print(sum1 % 100000)
    
# for 3 we have these combinations
# *   -   -
# -   *   -
# -   -   * 
# *   *   -
# *   -   *
# -   *   *
# *   *   *
# we have 7 combination here 2**3 is 8 since we never take  0 0 0 here thats why 2**n - 1

# for java BITINTEGER to be used in this q    
