# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

arr = list(map(int, input().split()))
s = input()
al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c = 0
mx = 0
print(len(s))
for i in range(len(s)):
    c = arr[al.index(s[i])]
    if c > mx : mx = c

print(mx*len(s)) 

''' Alternate with better TIME
maxi=0
for i in s:
    maxi=max(maxi,arr[ord(i)-97])          # 97 is ascii of 'a' we will subtract ascii of the character with 97 to get index
                                           # ord give us ascii value
print maxi*len(s) 
'''
