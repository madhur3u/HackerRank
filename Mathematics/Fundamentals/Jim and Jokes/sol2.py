# https://www.hackerrank.com/challenges/jim-and-the-jokes/problem

# this will check if the no. is legal for the given base
def checkbase(d,m):
    while d!= 0:
        r = d % 10
        d = d / 10
        if r >= m : return 0 # for a number to be legal in that base any of it digit should always be less than base
    return 1

# any base to decimal conversion
def decimalconv (d,m):
    if checkbase(d,m) == 0 : return 0
    s = 0
    p = 0
    while d != 0 :

        r = d % 10
        s = s + r * (m**p)
        p += 1
        d = d // 10

    return s

# main 
a = [0]*40 # made an array which will store the count of how many time we are getting same number after converting it in decimal
for _ in range(int(input())):

    m,d = map(int, input().split())
    a[decimalconv(d,m)] += 1        # taking the index as that number inc the count by 1 as we get that number since it is dates it will not be > 31 in decimal 

x = 0
for n in a[1:]: # now in this loop we check if the number has appeared more than 1 if yes then we find total no. of combinations
                # if we get 25 occurs 4 times then total jokes made using any 2 el at a time is 4C2 -> (4-1)(4)//2 combinations which we are doing below
    if n > 1:
        x += (n*(n-1))//2     # add up all combinations in x and final x will be the answer

print(x)    
