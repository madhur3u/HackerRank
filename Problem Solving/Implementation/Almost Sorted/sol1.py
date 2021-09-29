# https://www.hackerrank.com/challenges/almost-sorted/problem
# O(nlogn) due to sort

def check_sort(n, a):                                           # this will check if our array can be sorted using given constrains                                           
    
    sort_a = sorted(a)                                          # making a sorted array with which we will comapre
    c = 0                                                       # this will have count of numbers which are not in order as in sorted array
    index1 = index2 = 0                                         # these two will be index of left and rightmost element which are not in order

    for i in range(n):                                          # traverse through whole array

        if (a[i] != sort_a[i]) and c == 0 :                     # finding 1st index which is not in order as in sorted array (a[i] != sort_a[i])
            index1 = i                                          # c == 0 to keep only the leftmost index of that kind in it
            c = 1                                               # i will be the index and count of unordered element inc to 1
        
        elif (a[i] != sort_a[i]) :                              # this check other elements which are not in order
            index2 = i                                          # everytime a element is found, store it in index2
            c += 1                                              # increase count of unordered elements by 1
        
    if c == 0 :                                                 # if c == 0 means no elements were unordered i.e. array already sorted
        print ('yes')                                           
        return 
    
    elif c == 2 :                                               # if c == 2 means only 2 elements are unordered 
        print ('yes')                                           # so array can be sorted by swapping them    
        print (f'swap {index1 + 1} {index2 + 1}')               # print yes and index of elements (1 indexed)
        return
    
    elif c % 2 != 0 :                                           # if unordered elements are odd we can never have a swap as we need 2 elements for that
        print ('no')                                            # and also reverse can also be done only when unorderd elements are even (DRY RUN)
        return                                                  # so NO
    
    else :                                                      # now for case when c = 2,4,6,8...
        temp = a[ : index1] + \
               a[index1 : index2 + 1 : ][::-1] + \
               a[index2 + 1 : ]                                 # make a array with section from index1 to index2 reversed and rest same

        if sort_a == temp :                                     # check if this array equal to the sorted array or not
            print ('yes')
            print (f'reverse {index1 + 1} {index2 + 1}')
            return
        
        else :
            print('no')

# main
n = int(input())
a = list(map(int, input().split()))

check_sort(n, a)


