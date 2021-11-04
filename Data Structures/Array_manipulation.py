# https://www.hackerrank.com/challenges/crush/problem

n, q = map(int, input().split())
arr = [0]*(n+1)                               # make a array of length n+1 as in question 1 indexing so thats why n+1
max1 = 0                                      
x = 0

for _ in range(q):                            # run a loop for queries and take input
    a, b, k = map(int, input().split())

    arr[a] = arr[a] + k                       # adding  k to index a
    if (b+1) <= n : 
        arr[b+1] = arr[b+1] - k               # adding -k to index (b+1)

# Doing this kind of update, the ith number in the array will be prefix sum of array from index 1 to i because we are adding k to the 
# value at index a and subtracting k from the value at index b+1 and taking prefix sum will give us the actual value for each index after q operations  
      
# print(arr)
for i in range(1,len(arr)):

    x = x + arr[i]                            # calculating all prefix sum
    max1 = max(max1, x)                       # storing the max prefix sum

print(max1)

'''
n = 10, q = 3

a b   k
1 5   3
4 8   7
6 9   1

            1   2   3   4   5   6   7   8   9   10
1st query   3                  -3   
2nd                     7                  -7
3rd                             1               -1

a = [0      3   0   0   7   0   -2  0   0  -7   -1  ]

with this we can see that max sum would have been in 4th or 5th col where 3 and 7 both exist i.e. 10 and same will be
sum of 3 and 7 whch will be max sum of prefix in a

'''
