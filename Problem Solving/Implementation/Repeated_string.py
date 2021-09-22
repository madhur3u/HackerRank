# https://www.hackerrank.com/challenges/repeated-string/problem

s = input()
n = int(input())

a = s.count('a')
x1 = a*(n//len(s)) # this will give us min no. of a which can be present in final string

r = n % len(s)
x2 = s[0:r].count('a') # if string cut from between this will give us rest of a present till n % len(s)

print(x1 + x2)
