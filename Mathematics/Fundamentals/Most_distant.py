# https://www.hackerrank.com/challenges/most-distant/problem

import math

maxx = -10**10  # taking max and min value as per restrictions in the question
minx = 10**10
maxy = -10**10
miny = 10**10
for _ in range(int(input())):
  
    x, y = map(int, input().split())
    maxx = max (x, maxx)    # taking max value in x axis
    minx = min (x, minx)    # taking min value in x axis

    maxy = max (y, maxy)    # taking max value in y axis
    miny = min (y, miny)    # taking min value in y axis

# here we are taking all 6 possibility which can happen with the fiven 4 points using coordinate geometry formulas
    
a = [abs(maxx - minx), \   
     abs(maxy - miny), \
     math.sqrt(maxx**2 + maxy**2), \
     math.sqrt(maxx**2 + miny**2), \
     math.sqrt(minx**2 + maxy**2), \
     math.sqrt(minx**2 + miny**2)]

print(round(max(a),6))
'''
One of the coordinate will always be zero so it will always lie on axis
It is obvious that the most distant pair of dots have to be a pair from the following dots:

    highest
    lowest
    rightmost
    leftmost

You just have to find those 4 dots. Then, you must calculate the most distant pair in those dots. 
There are only 6 pairs, so this is fast. 
'''
