# https://www.hackerrank.com/challenges/sherlock-and-moving-tiles/leaderboard

L, s1, s2 = map(int, input().split())
q = int(input())

d = L*(2**(1/2))
s = abs(s1-s2)

for o in range(q):

    ar = int(input())
    l = (ar**(1/2))*(2**(1/2))
    t = (d - l)/s

    print(round(t,4))

# arrpoach -> we take the length of diagonal first then using length of diagonal we calculate how much difference
# is between both diagonals after t sec and make a formula
# sqrt(ar)*sqrt(2) = L*sqrt(2) - abs(s1 - s2)*time    now we calculate time using this 
#       l          =    d      -      s      *  t
# hence t = (d - l)/s
