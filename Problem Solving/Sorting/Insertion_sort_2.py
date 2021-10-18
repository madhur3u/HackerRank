# https://www.hackerrank.com/challenges/insertionsort2/problem
# just compare 2 values every time and check them, if not in order place value at i + 1 in order 

# def binarySearch(sub, val):
#     lo = 0
#     hi = len(sub)-1
#     while(lo <= hi):
#         mid = lo + (hi - lo)//2
#         if sub[mid] < val:
#             lo = mid + 1
#         elif val < sub[mid]:
#             hi = mid - 1
#         else:
#             return mid
#     # return low if not found
#     return lo

# def rotate1(a, lo, hi):
#     a = a[:lo] + [a[hi]] + a[lo:hi] + a[hi + 1:]
#     return a

# main
n = int(input())
a = list(map(int, input().split()))

# for i in range(n - 1):
    
#     if a[i] < a[i + 1] :
#         print(*a)
#         continue
#     else:
#         lo = binarySearch(a[:i + 1], a[i + 1])
#         a = rotate1(a, lo, i + 1)
#         print(*a)
        
for i in range(len(a) - 1):
    
    # key is the value to be checked every time
    # if not in order place it in order
    key = a [i + 1]     
    j = i
    
    # swap values till they are in order
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j = j - 1
    
    # at a[j+1] we place key
    a[j + 1] = key
    print(*a)
