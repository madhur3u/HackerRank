# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k, n):   
    x = 1
    i = 0
    i = (i + k)%n
    if c[i] == 1 : x = x + 2
    while i != 0:
        i = (i + k)%n
        x += 1
        if c[i] == 1 : x = x + 2
        if i == 0 : break
    return(100 - x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k, n)

    fptr.write(str(result) + '\n')

    fptr.close()
