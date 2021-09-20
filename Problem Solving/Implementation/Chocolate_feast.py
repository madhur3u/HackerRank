# https://www.hackerrank.com/challenges/chocolate-feast/problem

for _ in range(int(input())):

    money, cost, m = map(int, input().split())
    c = money // cost       # initial ch will be money by cost and same will be no. of wrappers
    r = c

    while r >= m:           # while rappers are greater than no. of wrapper req to buy a chocolate we run loop
        c = c + r//m        # c will in by no. of ch we can buy from wrappers
        r = r//m + r % m    # r will get new value which is no. left after buying chocolate + no. of new wrappers from new ch
    
    print(c)
