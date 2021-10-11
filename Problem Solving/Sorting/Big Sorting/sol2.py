# https://www.hackerrank.com/challenges/big-sorting/problem

n = int(input())
arr = [input() for i in range(n)]

# logic here is to use length of strings
# if we sort arr directly it dont compare whole string 
# so we create a dict in which key is length of string and value will have all those strng with that length
# now we sort our dictionary keys
# and since inside each key, length of values is same, so we can sort them without any problem as every char in st is comapred
# print the dict in inc order of keys

d = {}

for i in arr :
  
    key = len(i)            # key will be length of string
    
    if key in d:            # if key exist, add the string to array of values
        d[key].append(i)
    else :
        d[key] = [i]        # if key dont exist, make pair, with value in array

for key in sorted(d):             # sorting keys, so now we get key in increasing order
    for value in sorted(d[key]):  # now for a key, we sort the value array in that key
        print(value)              # print value
