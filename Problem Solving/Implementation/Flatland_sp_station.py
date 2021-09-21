# https://www.hackerrank.com/challenges/flatland-space-stations/problem
# nlogn but space is minimum

def maxd(n,m,a):
    
    if n == m : return 0                            # this means all cities have space stations so 0 
    
    a.sort()                                        # sort the array having list of cities with space station
    
    md = abs(0 - a[0])                              # finding out distance between 0th city and the 1st city in list with sp st
    md = max (md, abs(a[-1] - (n - 1)))             # same to be done with last city also, since we need max value of distance so find max
    
    for i in range(0,m-1):                          
        # print(1)
        tempd = (abs(a[i] - a[i+1]))//2             # now in the array if any city is skipped still distance will always be equal to (a[i] - a[i+1])//2 
        md = max (md,tempd)                         # compare to take max
    
    return md
    
n,m = map(int, input().rstrip().split())            # INPUT
a = list(map(int, input().rstrip().split()))

print(maxd(n,m,a))                                  # calling function
