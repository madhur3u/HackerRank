# https://www.hackerrank.com/challenges/harry-potter-and-the-floating-rocks/problem 
# https://www.hackerrank.com/challenges/harry-potter-and-the-floating-rocks/editorial

def gcd(x,y):
    while(y!=0):
        x,y=y,x%y
    return x

for _ in range(int(input())):
    
    x1,y1,x2,y2 = map(int, input().split())
    
    g = gcd (abs(x2-x1),abs(y2-y1))
    
    print(g-1)
    

# no. of integral points between two points is equal to gcd(x1-x2,y1-y2) - 1

'''
Assume the given points as P1(x1,y1) and P2(x2,y2).
x1,y1,x2,y2: integers

Let’s define the following variables:
dx=abs(x1 - x2). dy=abs(y1 - y2).
The number of integral points between P1 and P2 will be equal to gcd(dx,dy)-1.


Let the fraction a / b in its reduced form be the slope of the line joining P(x1 , y1) and Q(x2 , y2), 
which is equal to (y1 - y2) / (x1 - x2). To get all the points with integral coordinates, lying on the 
line PQ and between P and Q, we need to keep moving b units in the x-direction and a units in the 
y-direction, starting from P until we reach Q. So the number of such points (excluding P and Q) is 
given by n, where

    n = abs((y1 - y2) / a) - 1

or equivalently,

    n = abs((x1 - x2) / b) - 1.

However, since

    a = (y1 - y2) / g

and

    b = (x1 - x2) / g,

where

    g = gcd(y1 - y2 , x1 - x2),

we have

    n = abs(g) - 1,

and that's the answer we need.        '''
