# https://www.hackerrank.com/challenges/append-and-delete/problem

s = input()
t = input()
k = int(input())
c = 0
for i in range(min(len(s),len(t))):
    if s[i] == t[i] : c+=1
    else : break

x = len(s) - c + len(t) - c

if ((k == x or k >= len(s)+len(t))) : print('Yes') # if k = bache hue words or k is greater than lemgth of both string in 2nd case deletion can happen multiple times
elif(x%2 == k%2 and k >= x) : print('Yes') # if bache hue words x are odd then k should also be odd and vv and also k sholud be more than bache hue words or equal
else : print('No')
