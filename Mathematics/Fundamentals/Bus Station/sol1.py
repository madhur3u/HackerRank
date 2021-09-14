# https://www.hackerrank.com/challenges/bus-station/problem

n = int(input())
a = list(map(int, input().split()))
b = []
x = sum(a)
for i in range(max(a),(x//2) + 1,min(a)): 
    if(x % i == 0) : b.append(i)

# BRUTEFORCE KINDA

# what we are doing here (above) is finding factors of sum of a as bus can never be empty so the ans will atleast be a factor
# of sum(a). 1st value is length of biggest group as a bus length smaller than this is not possible cant take max(a) group
# till sum//2 as after that we will always get some seats empty in 2nd bus
# increase it by min(a) as less than that it will never be able to accomodate 2 or more groups comletely

for lbus in b:
    s = 0
    for i in range(n):
        s = s + a[i] # sum of all groups till i
        if (s == lbus): # if sum of groups is equal to lbus which is a factor we found above make s = 0 again
            s = 0
        
        if (s > lbus) : # if sum become greater that ln is not acceptable so break 
            c = 0
            break
    
    if (s == 0) : print(lbus,end =" ") # if s = 0 then it is value as inside 1st if we are doind s = 0 if lbus is the one

print(x) # one length will always be the total sum of all which we print in last
