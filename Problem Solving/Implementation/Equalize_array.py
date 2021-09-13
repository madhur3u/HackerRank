# https://www.hackerrank.com/challenges/equality-in-a-array/problem

n = int(input())
ar = list(map(int, input().split()))
b = [0]*101

for number in ar : 
    b[number] += 1 #will take count of occurence all numbers

print(n-max(b))
# all no. - sum of the max occurence
