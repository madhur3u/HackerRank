# https://www.hackerrank.com/challenges/encryption/problem

import math

s = input()
# x = math.floor(math.sqrt(len(s))) # taking floor and ceil as row and col mentioned in ques
y = math.ceil(math.sqrt(len(s))) # the code is working fine even without using floor

for k in range(y): # this loop runs for the no. of words we have to print seprated by space in new encrypted form
    code = ''
    for i in range(k,len(s),y): # this take out the new word which is the columns digit so we increment the range y times
        code = code + s[i]      # dtore it in a variable code and print after loop ends
    print(code,end=" ")
    

# print(sm[i::c],end=" ") alternate way to print the code without using a variable and inner loop (line 10 - 13)
