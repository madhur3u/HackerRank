# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
# The steps are fairly direct.

# (1) Compute the square of the original number.
# (2) Split it into two parts as described.
# (3) Check if they add up and equal the original number.
# (4) The number 1 might need to be handled separately.

def checkKap(n,d):                        # this func is taking squared value, and splitting in two with right side having d digits and adding them
    x = str(n)
    # print(x,d)
    if len(x) == 2*d:                     # adding when number length is 2 times d as for a square its length is always equal to 2d or 2d - 1
        n = int(x[0:d]) + int(x[d:])
    else : 
        n = int(x[0:d-1]) + int(x[d-1:])
    return n 
#     return the sum of digits
    

n1 = int(input())
n2 = int(input())

c = 0                                     # c initialize to check for INVALID RANGE
 
if n1 < 9 :                               # corner case if value is less than 9 print 1 (if n1 = 1) and make it 9 as 9 is the 2nd kap number
    if n1 == 1 : 
        print(1,end=" ")
    n1 = 9
    c = 1

if n2 >=9:                                # before 9 no other number exist than 1 so checking after 9
    for num in range(n1,n2+1):
        x = num * num                     # taking square
        y = checkKap(x,len(str(num)))     # storing value of sum taken from func in y
        if (y == num) : 
            print(num,end=" ")            # print num if it is equal to y  
            c = 1
            
if c != 1 : print('INVALID RANGE')        # INVALID RANGE when we do not ever get into loop or 1st if block so c = 0  
  
''' ALT PYTHON2 CODE

def isGood(x):
    if x <= 3:
        return x == 1
    y = str(x*x)
    d = len(str(x))
    r = int(y[-d:])
    l = int(y[:-d])
    return l+r == x

p = int(raw_input())
q = int(raw_input())

l = []
for i in xrange(p, q+1):
    if isGood(i): l.append(i)

if len(l) == 0:
    print "INVALID RANGE"
else:
    print ' '.join([str(x) for x in l])
'''
