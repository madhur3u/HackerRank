# https://www.codechef.com/problems/ADDNDIV

# Simpler approach (AC) :- eliminate all the prime factors of A which are common in both A and B , 
# i.e keep dividing A with GCD(A,B) untill GCD becomes 1 , now check if A is 1 then YES,   
# if it still has some prime factor left in it which is not in B then print NO

def gcd(x, y):                                      # GCD
    while y > 0:
        x, y = y, x % y
    return x

# main
for _ in range(int(input())):                       # test cases

    a, b = map(int, input().split())                # taking input a and b
    
    g = gcd(a, b)                                   # find GCD of two numbers

    while g != 1 :                                  # check till the GCD is not 1
        a = a / g                                   # update a by dividing it by GCD 
        g = gcd(a, b)                               # update new GCD
    
    if a == 1 : print('YES')                        # if a is 1 then we can get our answer
    else :      print('NO')

      
# here we need to add x = x + a till we get it equal to b**n
# so we need to check if b is divisible by all the prime factors of a or not, if it is then only we can get it equal to b**n
# taking out prime factors and then finding answer gave us TLE
# so we compute gcd which will also give us factor, and here we check if dividing by GCD multiple time is making a = 1 or not
