// https://www.hackerrank.com/challenges/p1-paper-cutting/problem 

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        long n = scn.nextInt();
        long m = scn.nextInt();
        System.out.println(n*m - 1); 
}

/* if n >= m
   (n-1) + n*(m-1) will give us answer on opening this we will get -> n*m - 1
   so we don't need to check which one is max and can directly get ans 
        PREVIOUS CODE :
        long n = scn.nextInt();
        long m = scn.nextInt();
        long max = Math.max(n,m);
        long min = Math.min(n,m);

        System.out.println((max - 1) + max*(min - 1)); */
