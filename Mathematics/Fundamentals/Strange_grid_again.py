# https://www.hackerrank.com/challenges/strange-grid/problem

r, c = map(int, input().split())

x = ((r - 1)//2) * 5 + c

if r % 2 == 0 : print(2*x - 1) 
else : print(2*x - 2)  

# use AP approach form a grid and try to find how AP is forming for consecutive rows
