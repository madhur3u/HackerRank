# https://www.hackerrank.com/challenges/constructing-a-number/problem

for _ in range(int(input())):
    l = int(input())
    arr = list(map(int, input().split()))
    
    total_sum = 0
    
    for i in arr:
        total_sum += i
    
    if total_sum % 3 == 0: print('Yes')
    else : print('No')
