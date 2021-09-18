# https://www.hackerrank.com/challenges/beautiful-triplets/problem

n, d = map(int, input().split())
a = list(map(int, input().split()))             # take the input as set rather than list 

# we are going to make a beautiful triplet by ourselves using one value of list (array) and
# next two values be +d and +2d
# So our subset will be {a[i] , a[i] + d , a[i] + 2*d} this subset is a beautiful triplet
# now we just need to find if this is a subset of our original set or not for that we are going to check
# if all the 3 values are present in our list or not
# if it exists in set then we found a beautiful triplet increase the counter

c = 0
for i in range(n-2):                            # n - 2 as we can not take last and 2nd last value as 1st value
    s = []
    s = [a[i] , a[i] + d , a[i] + 2*d]          # subset

    if (s[0] in a) and (s[1] in a) and (s[2] in a)  : c += 1

print(c)
