# https://www.hackerrank.com/challenges/absolute-permutation/problem

for _ in range(int(input())):

    n, k = map(int, input().split())

    if k == 0 : print(*[i+1 for i in range(n)])     # if k is zero print as it is from 1 to n

    elif n % (2 * k) != 0 : print(-1)

    else :
        add = True                  # always starts with i+k
        ans = []

        for i in range(1, n+1):
            if add:
                ans.append(i+k)
                
            else:
                ans.append(i-k)
                
            if i % k == 0:          # this is used to change value of add depending upon k, pair formation

                if add:             
                    add = False
                else:
                    add = True
        
        print (*ans)                # print list directly


# there are two exception cases, like below:
# 1.k == 0: print all the numbers from 1 to N
# 2.if (n / k) % 2 is not ZERO, print -1 (as this must be zero to be abolute permutation)

# Otherwise, follow the pattern below:

# if we go from 1 to N (i),
# Permutation is either i+k or i-k. It always starts with i+k.
# 1.Put i+k to permutaion for k times
# 2.Switch to i-k for k times
#     repeat 1 & 2 until the end.


# if n % (2*k) is not ZERO, print -1. That's because you'll need to "shuffle" groups of 2*k elements.
# For example, when n = 8 and k = 2, you'll start off with [1,2,3,4,5,6,7,8] and shuffle groups of 4 like this:

# 1 and 3
# 2 and 4
# -
# 5 and 7
# 6 and 8
# ...
# The approach works in this case because 8 is divisible by 4. Or more generally, it will work when n is divisble by 2*k.            
