# https://www.hackerrank.com/challenges/migratory-birds/problem

print("Hello world")
arr = [1,2,3,4,1,5,4,3,2,4,1,3,4]
arr.sort()
print(arr)
n = len(arr)
i = 0
c = 1
d = 0
n1 = 1
while i < n - 1 :
    if arr[i]==arr[i+1] :
        c = c + 1
    elif c > d :
        d = c
        n1 = arr[i-1]
        c = 1
    else :
        c = 1
        
    i = i + 1
    
print(n1)
