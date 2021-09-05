'''
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

    The elements of the first array are all factors of the integer being considered
    The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

https://www.hackerrank.com/challenges/between-two-sets/problem
'''

n1 , n2 = list(map(int, input().rstrip().split()))
arr1 = list(map(int, input().rstrip().split()))
arr2 = list(map(int, input().rstrip().split()))

# Function to find HCF Using Euclidian algorithm
def LCM(x, y):
    lcm = x * y
    while(y):
       x, y = y, x % y
    lcm = lcm // x
    return int(lcm)
def HCF(x, y):
    while(y):
       x, y = y, x % y
    return x
x = arr1[0]
y = max(arr2)
for i in range(n1) : x = LCM (x, arr1[i])
for i in range(n2) : y = HCF (y, arr2[i])

i = x
c = 0
while i <= y :
    if(y % i == 0) :
        c = c + 1
    i = i + x
        
print(c)
