# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.
# https://www.hackerrank.com/challenges/picking-numbers/problem

n = int (input())
a = list(map(int, input().split()))
a.sort()
i = 0
co = []
while i < n-1 :
    d = 0
    c = 0
    j = i + 1
    id1 = []
    while d <= 1 :
        try : 
            d = abs(a[i] - a[j])
            if(d>=1) : id1.append(j)
            c += 1
            j += 1
        except :
            i = n
            break
    try : i = id1[0]
    except : i += 1
    co.append(c)

if abs(a[-1]-a[-2]) <= 1 : co[-1] = co[-1] + 1 # corner case as it is not comparing 2nd last and last value in prg
print(max(co))

'''
ALTERNATE JAVA SOLUTION

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[100];
        for(int a_i=0; a_i < n; a_i++){
            a[in.nextInt()]++;
        }
        int max = 0;
        for (int i = 0; i < 99; i++) {
            max = Math.max(max, a[i]+a[i+1]);
        }
        System.out.println(max);
    }
}
'''
