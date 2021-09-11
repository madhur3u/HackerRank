#### https://www.hackerrank.com/challenges/even-odd-query/problem

n = int(input())
a = list(map(int, input().split()))

for i in range(int(input())):
    
    x,y = map(int, input().split())
    
    if (a[x-1] % 2 == 0):
        if(x < y and a[x]==0): print('Odd') #odd
        else : print('Even') #even
    else : print('Odd') #odd
