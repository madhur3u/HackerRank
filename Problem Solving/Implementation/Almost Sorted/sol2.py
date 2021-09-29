# https://www.hackerrank.com/challenges/almost-sorted/problem

def is_sorted(n, a):            # this fn checks if an array is sorted or not

    for i in range(n-1):
        if a[i] > a[i + 1]:             
            return False        # if a element in left is bigger than right element then it is not sorted so False
    return True                 # if we never encounter a situation like above ever, True

def check_sort(n, a):                                                                     
    
    # if array already sorted we just return yes
    if (is_sorted(n, a)) :                      
        print ('yes')
        return

    # now if array is not sorted we need to find the index 
    # for a element to be a part of sorted array it need to follow this condition (a[i-1] < a[i] < a[i+1])
    # so we traverse from 1 to end and find the 1st element which do not satisfy this condition
    # this will be our index1
    for i in range(1,n-1):
        if not (a[i-1] < a[i] < a[i+1]) :
            index1 = i
            break
    
    # similiarly now we traverse from end to 0 and find the rightmost element which do not satisfy condition
    for i in range(n-2, 0, -1):
        if not (a[i-1] < a[i] < a[i+1]) :
            index2 = i
            break
    

    # 1st checking if we can get answer with swap or not
    # make a temporary array and swap the values at indices we got
    # and check if the swapped array is sorted or not
    temp = a[:]
    temp[index1], temp[index2] = temp[index2], temp[index1]

    if (is_sorted(n, temp)) :
        print ('yes')
        print (f'swap {index1} {index2}')
        return


    # now if array is not sorted after swapping, it will come here
    # now we will reverse the array portion from index1 to index2
    # and check if our array is sorted or not
    temp = []
    temp = a[ : index1] + a[index1 : index2 + 1 : ][::-1] + a[index2 + 1 : ]
    
    if (is_sorted(n, temp)) :
        print ('yes')
        print (f'reverse {index1} {index2}')
        return
    
    # if we never get a sorted array
    print('no')
    return 
    

# main
n = int(input())
a = list(map(int, input().split()))

a = [-1] + a + [1000000000]             # here we add border to array with min-1 and >max number to deal with out of index problem
n = n + 2                               # this will also make our original array one indexed

check_sort(n, a)

