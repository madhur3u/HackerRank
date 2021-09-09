# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

i, j, k = map(int, input().split())
c = 0
for o in range(i, j+1) :
    
    n = len(str(o))
    s = 0
    x = o
    while x != 0 :
        r = x % 10
        x = x // 10
        s = s + r*(10**(n - 1))
        n -= 1

    if abs(o - s) % k == 0 : c+=1
print(c)

''' Alt PYTHON sol using String Operations

i,j,k = [int(x) for x in input().split()]
count = 0
for x in range(i,j+1):
    if (x - int(str(x)[::-1])) % k == 0:
        count += 1
print(count)
'''
