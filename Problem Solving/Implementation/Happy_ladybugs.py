# https://www.hackerrank.com/challenges/happy-ladybugs/problem

# A few things to consider:
# 1) If there is at least one empty cell, then it is always possible to move any bug to any cell.
# 2) If a ladybug's color is unique in the set, the ladybug will never be happy.
# 3) Initially if all the bugs are happy then there is no need to make any move.

for _ in range(int(input())):

    n = int(input())
    s = input()

    c = 0
    if s == "_":                  # corner case 1 when only one blank present answer always yes                      
        print("YES")
        continue                  # continue will go to for loop again and take next input in next iteration 

    if n == 1:                    # corner case 2 when only 1 ladybug answer always no as no pair form
        print("NO")
        continue

    if "_" not in s:              # when no blank space present means we cannot arrange ladybugs so checking if they are already arranged

        if s[0] != s[1]:          # corner case 1 in this to check if 1st and 2nd ladybug form a pair or not, if no print NO and continue to next iteration

            print("NO")
            continue

        if s[-1] != s[-2]:        # corner case 2 in this to check if last and 2nd last ladybug form a pair or not

            print("NO")
            continue

        for i in range(1, n - 1):                       # this for loop run from 2nd to 2ndlast ladybug

            if s[i - 1] != s[i] and s[i + 1] != s[i]:   # and check if pair is there or not

                print("NO")
                c = 1
                break

        if c == 0:                # if c == 0 means we never find any unpaired ladybug so print YES
            print("YES")
            continue

    else:                                               # when blank is present
        alpha = [0] * 26                                # make a array to store count of alphabets thats why 26 elements

        for i in range(n):
            if s[i].isupper():                          # when we encounter an alphabet 
                alpha[ord(s[i]) - 65] += 1              # make counter of that alphabet increase by one // ord('') give us ASCII values, 'A' = 65
                
        if 1 in alpha:                                  # if an alphabet is present only once it can never form pair 
            print("NO")
        else:
            print("YES")
