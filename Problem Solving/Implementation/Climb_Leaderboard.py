## https://www.hackerrank.com/challenges/climbing-the-leaderboard/leaderboard

n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))

''' OLD METHOD WAS WORKING BUT TLE IN SOME CASES
a.append(0)

for j in range(n2):
    r = 1
    for i in range(n1):
        if(b[j]>=a[i]) : break
        else :
            if(a[i]!=a[i+1]): r+=1
    print(r)
'''
lb = sorted(set(a), reverse = True) # set will delete the repititive elements and sort 
l = len(lb)

for a in b :
    while l > 0 and a >= lb[l-1] : l = l - 1
    print (l + 1)
