# https://www.hackerrank.com/challenges/big-sorting/problem

n = int(input())
arr = [input() for i in range(n)]

# if we have sorted it directly using str->int tle
# so we convert that inside when sorting, make it mush faster, usinf key = int
arr.sort(key=int)
for i in (arr):
    print(i)

'''

Some speculate that sort() is faster than sorted(), but these functions are basically the same except the former 
is an in-place sort (which shouldn't matter here).
Edit: sorted() is a wrapper for sort(). See also: https://stackoverflow.com/questions/1915376/is-pythons-sorted-function-guaranteed-to-be-stable

Analysis with cprofile kept reporting that print() was the cause of the slowdown, which made no sense at first.
It turned out that int -> str conversions (whether by print or explicitly converting the values first) are surprisingly costly 
(probably far more costly with huge integers, as test cases #4, #5, and #6 appear to contain). 
If you're taking the "convert to int, sort, then print" route, you're actually printing ints, 
which are converted internally to strings for display. And that's why print becomes slow.

First, a typical slow implementation 
(I originally had a longer form for these - the list comprehension here makes it more compact but not noticeably faster):

for i in sorted([int(s) for s in unsorted]):
    print(i) # int to str = costly

Adding an int -> str conversion before print doesn't help - in fact, it gets a little bit slower:

for i in sorted([int(s) for s in unsorted]):
    s = str(i) # This is a costly step
    print(s)
_____________________________________________________________________________________________________________________________________________________

However, using the key=int sorting argument performs the necessary conversions internally during the sort process itself, 
while returning the original string values that are quickly printed. (Note that the argument to key is the name of a function that takes one argument, 
in this case int().) I'm going to guess that str -> int is much faster than int -> str

A fast (challenge-friendly) in-place sort():

unsorted.sort(key=int)
for s in unsorted:
    print(s)

sorted() is virtually the same speed, and doesn't modify unsorted:

for s in sorted(unsorted, key=int):
    print(s)


More info:

    https://docs.python.org/3.6/library/functions.html?highlight=sorted#sorted
    https://docs.python.org/3.6/library/profile.html#profile.Profile

'''
