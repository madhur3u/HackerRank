# https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/lola-and-candies-36b57b1b/

sum = int(input())                      # input will be sum of consecutive numbers
count = 0               
if sum % 2 == 0 : N = 2                 # if sum is even no. of terms will also be even as all terms are odd in array
else : N = 1                            # no. of terms for odd sum

while True:                             

    # print(f'Iteration no. {N}')
    a = (sum - (N-1)*N) / N             # formula made using sum of AP of odd series where N is no. of terms which we iterate
    N = N + 2                           # inc no. of terms

    if a < 1 :                          # loop will run till a >= 1 as a which is 1st term of series will always be >= 1
        break

    if a % 2 != 0 and a % 1 == 0 :      # if a is integer a % 1 == 0, and odd then count is inc
        count += 1

print(count)

'''
Sum of AP = n*(2*a + (n-1)*d) / 2 

here the series is 1,3,5,7,9,11..... where d = 2, and a will always be a odd number, and Sum is given to us

therefore , a = (sum - (N-1)*N) / N , now we need to find how many times we have odd and integer a, that will be count
'''
