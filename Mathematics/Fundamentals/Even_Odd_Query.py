#### https://www.hackerrank.com/challenges/even-odd-query/problem

n = int(input())
a = list(map(int, input().split()))             # array is one indexed

for i in range(int(input())):
    
    x,y = map(int, input().split())
    
    if (a[x-1] % 2 == 0):                       # this will check if the number whose power is to be raised is even
        
        if(x < y and a[x]==0): print('Odd')     # odd, acc to query it will do ans for y >=x, so here we check if it go to next iteration and 
                                                # the next number is zero, then it is odd as n**0 = 1, always odd
        else : print('Even')                    # even, if next number is not zero, or query never go to second iteration to fetch 2nd number, at that case 1 return
   
    else : print('Odd')                         # odd, if base number is odd irrespective of any positive number in power

        
# find(int x,int y)                   this was the query fiven to us, this query performs recursion to find power
# {                                       
#     if(x>y) return 1;               when y>x ans returns 1
#     ans = pow(A[x],find(x+1,y))     recursion
#     return ans
# }
# y >= x initially constrain
