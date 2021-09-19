# https://www.hackerrank.com/challenges/minimum-distances/problem
# Try using dictionaries and hashmap also after learning

n = int(input())
a = list(map(int,input().split()))
min1 =  n 
for i in range (n-1):
    try : 
        x = (a[i+1:].index(a[i]) + i + 1) - i   # the 1st part give us the index of a[i] if it occurs in list again 
                                                # after ith position hence we have shorten the list and since we shorten 
                                                # the list the index it will provide will be according to the length of the
                                                # new list so we are adding i + 1 to get original index of that element in our INPUT list
        min1 = min(min1, x)
        
    except : continue

print(min1 if min1 < n else -1)             # this is how we use ternary operator in python it will print min1 if the if condition is true else it prints -1
