# https://www.hackerrank.com/challenges/lisa-workbook/problem

n,k = map(int, input().split())
a =list(map(int, input().split()))
                          
c = 0
pg = 1

for i in range(n):                    # reading one chapter at a time

    low = 1                           # this will tell us the 1st question in a page
    high = low + 1                    # last ques in a page 
    
    if a[i] <= k :                    # thsi is for case when no. of ques in chapter (a[i]) are less than or equal to max no. of q in a page k
        low = 1                       # for this case low will always be 1 and high will always be the max no. of ques in that page i.e. a[i]
        high = a[i]

        # print(f"{low}\t{high}\t{pg}")

        if pg in range(low,high+1) :  # if page is in range of question then counter inc
            c += 1
        
        pg += 1                       # pg will inc as we have read a page

    else :
        while a[i] > 0:                                 # for case when no. of ques in a chapter is greater than k

            if (a[i] < k) : high = low + a[i] - 1       # changing value of high depending upon a[i], low is added as high will always be gr than low
            else : high = low + k - 1

            # print(f"{low}\t{high}\t{pg}")

            if pg in range(low,high+1) :              
                c += 1
            pg += 1                                     # update page
            low = high + 1                              # updating low as next ques which will be on next page so high + 1

            a[i] = a[i] - k                             # update remaining question in a chapter


print(c)    
        
  
'''
in this low will give us the 1st question which will be on a page and high will give us the number of last question we have
in the page and pg is the page number when our pg is in range of low and high we inc the counter


OUTPUT OF LOW HIGH AND PG FOR EACH PG NO.
10 5
3 8 15 11 14 1 9 2 24 31   INPUT

low    high     pg
1       3       1
1       5       2
6       8       3
1       5       4
6       10      5
11      15      6
1       5       7
6       10      8
11      11      9
1       5       10
6       10      11
11      14      12
1       1       13
1       5       14
6       9       15
1       2       16
1       5       17
6       10      18
11      15      19
16      20      20
21      24      21
1       5       22
6       10      23
11      15      24
16      20      25
21      25      26
26      30      27
31      31      28
'''
