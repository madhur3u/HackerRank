# https://www.hackerrank.com/challenges/non-divisible-subset/problem

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0]*k  # array to store count of remainder of all no.s by dividing them by k

for number in a:
    b[number % k] += 1  # storing count of a remainder i.e. how many times a remainder apper in the array
    
''' For any number K, the sum of 2 values (A & B) is evenly divisible by K if the sum of the remainders of A/K + B/K is K.
(There is also a special case where both A & B are evenly divisible, giving a sum of 0.)
For any such remainder, there is 1 and only 1 other remainder value which will make a sum divisible by K. '''


c = min(b[0], 1) # if a no. which give remainder 0 is present we take that number only once else the sum of 2 no. will be divisible by k
                 # so here we take min of b[0] with 1 if no value is present i.e. 0 we get c = 0 else c = 1

for i in range(1, k//2 + 1): # remainder pairs repeat after k//2 so just check the remainder pair before half
    if i != k - i:           # for EVEN k
        c += max(b[i], b[k-i])  # we only have to take one from pair so we take the maximum one using k - i as k-i is the pair of i remainder
        
if (k % 2 == 0 and b[k // 2] > 0): # if k is even we have a remainder which is not in pair ex. 3 for 6, so we only have to take it one time if it exists
    c += 1

print (c) # biggest subset
