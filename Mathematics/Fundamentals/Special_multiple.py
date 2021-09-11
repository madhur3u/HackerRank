# https://www.hackerrank.com/challenges/special-multiple/problem

def db(n): # func for decimal to binary
    return int("{0:b}".format(int(n)))

a = []
for i in range(1,5000): # this create a array of 1st 5000 numbers like we need 
    a.append(db(i)*9)
    
for q in range(int(input())):
    n = int(input())
    for i in a :
        x = i
        if(i % n == 0) : break
        
    print(x)
