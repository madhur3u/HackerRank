# https://www.hackerrank.com/challenges/acm-icpc-team/problem

def acmTeam(a,n):
    # Write your code here
    l =[]     # array to store no. of topics a team knows
    #print(n)
    for i in range(n-1):
        for j in range(i+1,n):
            x = a[i] + a[j]     # add two individual to get how many topics are known if the form a team
            #print(x)
            l.append(len(str(x))-str(x).count('0'))  # total number of common topics will be 1 or 2 after adding so we just need to subtract
                                                     # the no. of zero in x to get no. of topics a team knows
    print(max(l))  # max no. of topics 
    print(l.count(max(l)))  # no. of teams who knows those no. of topics

#main
n,m = map(int, input().split())
arr =[]
for i in range(n):
    arr.append(int(input()))
#print(arr)
acmTeam(arr,n)
