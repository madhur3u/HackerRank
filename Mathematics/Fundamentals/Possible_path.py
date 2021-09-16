# https://www.hackerrank.com/challenges/possible-path/problem

def gcd(x,y):
    while(y!=0):
        x, y = y, x % y
    return abs(x)

for _ in range(int(input())):

    # steps we can go are 
    # (a + b , b)
    # (a , a + b)
    # (a - b , b)
    # (a , b - a)
    # add all x and y elements here we get (4a , 4b)
    ''' According to the definition of Greatest Common Divisior, if m is any integer, 
    then gcd(a + m * b, b) = gcd(a, b). (In this particular problem m = 1 or m = -1 in each step.) 
    Therefore, the gcd of (a + b, b), (a, a + b), (a - b, b) and (a, a - b) will be the same as the 
    gcd of (a, b). Therefore, in order to move to the target point, the gcd of the target point should 
    be equal to the gcd of the starting point. '''

    x1,y1,x2,y2 = map(int, input().split())
    if gcd(x1, y1) == gcd(x2, y2) : print('YES')
    else : print('NO')
