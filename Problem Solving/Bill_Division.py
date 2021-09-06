# https://www.hackerrank.com/challenges/bon-appetit/problem

n, k = list(map(int, input().rstrip().split()))
bill = list(map(int, input().rstrip().split()))
b = int(input())

bill.pop(k)
c = sum(bill) // 2
if b == c : print('Bon Appetit')
else : print(b - c)
