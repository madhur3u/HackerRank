# https://www.hackerrank.com/challenges/manasa-and-stones/problem

for _ in range(int(input())):
    
    n = int(input())                      # inputs
    a = int(input())
    b = int(input())
    
    n = n - 1                             # in the question 1st pos is always taken by 0 so we have to arrange a,b in n-1 places so changed n
    a,b = min(a,b),max(a,b)               # we need to print values in asc order so taking min value in a and max in b
    
    if a == b : print(a * n)              # when a and b are equal we will only have one distinct answer a*n
    
    else:
        
        for i in range(0,n+1):            # now we will traverse for all values of n we have to arrange a,b in n places so total n+1 iterations
            
            s = a * (n - i) + b * i       # see below explanantion
            print(s, end=' ')
        
    print()                               # this print is to go to next line in the end                  
            
'''          
n = 5

n = 4               as n = n-1
a = 10, b = 100     arranged min = a, max = b

                  i   sum

10  10  10  10    0   40   a*4 + b*0     these are ways in which we can arrange a and b in 4 places to get distinct values 
10  10  10  100   1   130  a*3 + b*1     there are total 5 ways (n+1)
10  10  100 100   2   220  a*2 + b*2
10  100 100 100   3   310  a*1 + b*3     s = a * (n - i) + b * i    // as in 1st iteration i is zero so we will only have a elements n-i  
100 100 100 100   4   400  a*0 + b*4
    
'''
    
