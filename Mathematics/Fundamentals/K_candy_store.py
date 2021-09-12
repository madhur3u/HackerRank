# https://www.hackerrank.com/challenges/k-candy-store/problem

def fact(n):
    f = 1
    for i in range(1,n+1) : f*=i
    return f

for _ in range(int(input())):
    n = int(input())
    k = int(input())

    # combinations with repititions n+k-1 C n-1 or C(n+k-1,n-1)

    s = fact(n+k-1) // (fact(n-1)*fact(k))
    print(s % 1000000000)

'''
Combination With Repetition      https://www.superprof.co.uk/resources/academic/maths/probability/combinatorics/combinations-with-repetition.html

Let suppose there are p elements in a set A. We are asked to select q elements from this set,
given that each element can be selected multiple times. This is known as a combination with repetition.
For instance, we can make combinations of three elements of the set {p, q, r, s} in this way:

ppp, ppq, ppr, pps, pqq, pqr, pqs, prr, prs, pss, qqq, qqr, qqs, qrr, qrs, qss, rrr, rrs,rss, sss

You can see that most of the alphabets are repeated more than once.

C(n+k-1,n-1)

'''
