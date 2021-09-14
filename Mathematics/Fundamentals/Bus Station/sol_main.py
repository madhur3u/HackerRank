# https://www.hackerrank.com/challenges/bus-station/problem

import math

n = int(input())
a = list(map(int, input().split()))
b = []
x = sum(a)
for i in range(1,int(math.sqrt(x)) + 1): 
    if(x % i == 0) : 
        b.append(i)
        if(i != x/i) : b.append(x//i) # for perfect sq we may get i and x/i same so this will ensure only one value go in list

b.sort() # now b has all factors from 1 to x

# what we are doing here (above) is finding factors of sum of (a) as bus can never be empty so the ans will atleast be a factor
# of sum(a). we have to sort the factors as ans should be printed in inc order


for lbus in b:  
    if lbus < max(a) : continue # it should be at bigger than max(a) else the bus can never be able to accomodate that group

    s = 0
    for i in range(n):
        s = s + a[i] # sum of all groups till i
        if (s == lbus): # if sum of groups is equal to lbus which is a factor we found above make s = 0 again
            s = 0
        
        if (s > lbus) : # if sum become greater that ln is not acceptable so break 
            break
    
    if (s == 0) : print(lbus,end =" ") # if s = 0 then it is value as inside 1st if we are doind s = 0 if lbus is the one
