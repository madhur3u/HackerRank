# https://www.hackerrank.com/challenges/reduced-string/problem

# Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. 
# In each operation, select a pair of adjacent letters that match, and delete them.
# Delete as many characters as possible using this method and return the resulting string. 
# If the final string is empty, return Empty String

# aaabccddd → abccddd → abddd → abd
# aa → Empty String
# baab → bb → Empty String

def delete_adjacent(a):
    a += '0'                        # adding a temp element to a at end to cover index out of range problem
    
    i = 0                   
    while (i < len(a) - 1):         # iterate from i = 0 till end and check if adjacent chars equal or not
        
        if (a[i] == a[i+1]):        # when adjacent chars equal
            
            a = a[:i] + a[i+2:]     # remove those chars from string using string slicing
            
            if i == 0 :             # now we ned to reduce i by 1, as we must check if after removing the 2 chars if we got one more pair from i - 1 and i + 2
              i = 0                 # so if i was originally 0 dont reduce it 
            else :                  # but if i was > 0 reduce i by 1
              i = i - 1             # cover up for cases like --> baab → bb → Empty String

        else : i+=1                 # else increase i
    
    return a[0 : len(a) - 1]        # removing the temp element and return a
        
# main    
s = input()
s = delete_adjacent(s)

print('Empty String') if s == '' else print(s)

