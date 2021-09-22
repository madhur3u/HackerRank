# https://www.hackerrank.com/challenges/fair-rations/problem

n = int(input())
a = list(map(int, input().split()))

if sum(a) % 2 != 0 :              # this means there are odd number of odd numbers so we cannot achieve required case 
    print('NO')                   # as to make every no. even with given conditions the no. of odd number should always be even
    
else:
    count = 0
    for i in range(n-1):          # iterate through loop till 2nd last element
        
        if a[i] % 2!= 0 :         # if the no. in array is odd
            a[i] += 1             # make that number even by adding 1
            a[i+1] += 1           # acc to given condition we are going to add 1 to next element also
            count += 2            # 2 are added so inc count by 2

    print(count)
