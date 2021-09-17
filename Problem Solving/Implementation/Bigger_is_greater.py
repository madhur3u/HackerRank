# https://www.hackerrank.com/challenges/bigger-is-greater/problem
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

for _ in range(int(input())):
    a = list(input().strip()) # taking a string input an converting to list
    # print(a)
    
    # find non increasing suffix
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i] : i -= 1
    # print(i)     
    
    if i <= 0 : print('no answer')

    else:

        for j in range(len(a)-1,i-1,-1):
            # print(j)
            if a[j] > a[i-1]: # find successor to the left element of the suffix, means find an element greater than the element left of non increasig suffix
                #print(1)
                a[j],a[i-1] = a[i-1],a[j] # swap the elements
                a[i:] = a[len(a)-1 : i - 1 : -1] # reverse the whole list from non inc suffix point till end
                break

        print(''.join(a)) # making list a string
