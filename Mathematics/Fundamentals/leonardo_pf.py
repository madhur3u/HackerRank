# https://www.hackerrank.com/challenges/leonardo-and-prime/problem

def isprime(n) :
    if(n <= 1): return False
    if(n <= 3): return True
    if(n%2 == 0 or n%3 == 0) : return False
    # the above condition will chexk for all number below 25 as our main below loop is starting from when n = 25 or
    # greater. Every value between 4 - 24 is either divisible by 2 or 3 else it is a prime number
    # also it will check all even numbers so now we check all odd no. >24

    i = 5
    while i*i <= n : # this loop work for n>=25 rest all cases tested above

        if(n % i == 0 or n % (i+2) == 0) : return False
        i = i + 6 # we are doing i + 6 to check if the no. is divisible by any prime no. or not

    return True        

q = int(input())
for j in range(q):
    c = 0
    d = 2
    n = int(input())
    if n <= 1 : print('0')
    if n == 2 : print('1') # corner cases
    for i in range (3,n+1,2):
        if (isprime(i)):
            d = d * i
            c = c + 1
        if d > n :
            print(c)
            break
  
# a = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79] we can make a array of prime no. rather than checking for
# all the values as the product will never be so big that we will have to check for every number >80 
