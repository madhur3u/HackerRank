# https://www.hackerrank.com/challenges/special-multiple/problem

def db(n):                               # func for decimal to binary
    return int("{0:b}".format(int(n)))

a = []
for i in range(1,5000):                  # this create a array of 1st 5000 numbers like we need 
    a.append(db(i)*9)
    
for q in range(int(input())):
    
    n = int(input())
    
    for i in a :                         # iterating in our arrays of 9's 
        if(i % n == 0) :                 # if the i is divisible bt N so we found our answer
            print(i)
            break
        

# binary digits 1-8
# 000 
# 001
# 010
# 011
# 100
# 101
# 110
# 111

# so we can find binary of a number and multiply it by 9 so we will get all combinations of number with 0-9 till 5000 here
