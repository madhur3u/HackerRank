# https://www.hackerrank.com/challenges/the-grid-search/problem

# QUESTION MAY LOOK EASY AT FIRST BUT THERE ARE MANY CASES WHICH NEED TO BE TAKEN CARE OF

# 1234567890  given 2D array
# 0987654321  
# 1111111111  
# 1111111111  
# 2222222222 

# 876543      to find if this small 2d array exist inside main array or not
# 111111  
# 111111

for o in range(int(input())):                             # no of test cases 
    
    main_row, main_col = map(int, input().split())
    a = [input() for i in range(main_row)]                # main array input       
    
    row, col = map(int, input().split())
    query = [input() for i in range(row)]                 # query is the array we need to search in main array

    x = False                                             # variable for checking if 
    
    for i in range(main_row - row + 1):                   # iterating through rows of main array, -row+1 is done as we have some height of other array so no use of iterating after that

        line_check = 0                                    # this checks if a row (line) inside main array matched with a row (line) of query

        if query[0] in a[i]:                              # checking if 1st row of query exists in a[i] main array ith row

            index = a[i].index(query[0])                  # if present we take out the index at which we found that
            while query[0] in a[i][index:]:               # iterate till we can find query[0] in that row but we will increase the index from where we are checking in main row
                                                          # this is done as there can be multiple instances eg, query = 99 and row is 991299 so we have 99 2 times in a row so need to check for both
                
                if query[0] in a[i][index:index+col]:     # this check if query[0] is in a[i] or not checking it here again for just next col digits as in 991299 when while loop check for 1299 
                                                          # it will move forward and 12 the next col length has to be rejected
                    line_check = 1                        # 1st query row found so inc line check
                    k = 1                                 # k is the index of query already checked for 0 so now 1

                    try :
                        for j in range(i+1,i+row):        # this is iterating for row - 1 no. of rows that is total no. of rows in query array -1 , -1 as we have already checked 0th row

                            # print(k,line_check, query[k], a[j][index:index+col])

                            if query[k] in a[j][index:index+col] :    # if query row exist in main row, [index:index+col] this ensure we always check below the previous main row index only where we 
                                                                      # found our 1st query row
                                line_check += 1                       # if row found inc line check
                            
                            k=k+1                                     # inc index of query array to check for next query row in next iteration

                        index = index + 1                             # index will be inc to 1 to check same row but now ahead of what we checked till now
                        
                    except:                                           # to handle exceptions when index out of range encounters
                        index = index + 1                             # index will be chnaged
                        continue                                      # continue the loop
                    
                    if line_check == row :                            # if we found our query then line check should be equal to no. of rows of query
                        x = True                                      # flag set to true
                        print('YES')  
                        break                                         # break out of loop
                
                else : index = index + 1                              # index will be increased for next while loop iteration
        
        if x == True:                                       # if flag true means we already found our ans so no need to check more rows so break
            break

    if x == False : print('NO')                             # if we never got ans flag will remain false only so print NO
