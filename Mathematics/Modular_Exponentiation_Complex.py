# https://www.hackerrank.com/challenges/russian-peasant-exponentiation/problem
# https://www.geeksforgeeks.org/modular-exponentiation-of-complex-numbers/

# read MODULAR EXP and russian peasent method for real no. to understand this better

def COMPLEX_MULTIPLY(x1,y1,mod): # to multiply two complex numbers x1 and y1 % mod
    # (a + bi) * (c + di) = (ac - bd) + i(ad + bc)
    a1 = ( (x1[0]*y1[0]) % mod - (x1[1]*y1[1]) % mod + mod ) % mod # +mod in end so it is always positive
    a2 = ( (x1[0]*y1[1]) % mod + (x1[1]*y1[0]) % mod ) % mod

    return [a1,a2]

def EXPONENTIATION(x,y,mod):
    res = [1, 0] # this will be our result initial value 1 + 0i
    #print (x,y,mod)
    while y > 0 :

        if y % 2 != 0 : # for y odd we will update res
            res = COMPLEX_MULTIPLY(res,x,mod) # if y odd then multiply res by x since it is compelex no.
                                              # so we defined a func to multiply two complex numbers
            #print (res)
        
        y = y//2
        x = COMPLEX_MULTIPLY(x,x,mod) # x * x at each step complex
    
    return res 

# main driver code
for _ in range(int(input())):

    a,b,y,mod = map(int,input().split())
    x = [a,b]
    # to find ((a+ib)**y)%mod
    # RUSSIAN PEASENT EXPONENTIATION METHOD IN COMPLEX

    x = EXPONENTIATION(x,y,mod)
    print(x[0],x[1])
    # print(str(x[0]) + " + " + str(x[1]) + "i")
    
'''   THIS WORK FOR ALL TEST CASES IT IS SAME THOUGH -_-
def mul(a,b,m):

    x=a[0]*b[0]-a[1]*b[1]
    y=a[0]*b[1]+a[1]*b[0]
    x%=m
    y%=m
    if x<0:x+=m
    if y<0:y+=m
    return (x,y)

def Pow(a,k,m):

    r=(1,0)
    while k:
        if k&1:
            r=mul(r,a,m)
        a=mul(a,a,m)
        k//=2
    return r

for _ in range(int(input())):
    a,b,k,m=map(int,input().split())

    res=Pow((a,b),k,m)
    print (res[0],res[1])
    
'''
