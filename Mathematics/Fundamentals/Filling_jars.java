// https://www.hackerrank.com/challenges/filling-jars/problem

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        long n = scn.nextLong();
        long m = scn.nextLong();
        long s = 0;
        for(long i = 1; i<=m; i++){

            long a = scn.nextLong();
            long b = scn.nextLong();
            long k = scn.nextLong();

            s = s + (b-a+1)*k;

        }
        s = s / n;
        System.out.println(s);

    }
}
