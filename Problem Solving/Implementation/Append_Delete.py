# https://www.hackerrank.com/challenges/append-and-delete/problem

s = input()
t = input()
k = int(input())
c = 0
for i in range(min(len(s),len(t))):         # this will check how many characters in both strings are same
    if s[i] == t[i] : c+=1                  # c will give us no. of same characters in s and t
    else : break
                                            # x will gives us all remaining different characters in both strings (x = bache hue words)
x = (len(s) - c) + (len(t) - c)             # (len(s) - c) are remaining diff characters in s,(len(t) - c) are remaining diff characters in t
                                            
if ((k == x or k >= len(s)+len(t))) :       # if k = bache hue words or k is greater than length of both string in 2nd case deletion can happen multiple times
    print('Yes') 
    
elif(x%2 == k%2 and k >= x) :               # if bache hue words are odd then k should also be odd and vv and also k sholud be more than bache hue words or equal
    print('Yes') 
    
else : print('No')

'''    
Case 1: If k=count then k appends or If k>=n1+n2 then any no. of deletions can be done.
Case 2: If count & k are both even/odd and count<=k then delete and append until steps=k.
Case 3: Or else it can't be converted into k steps.
'''
