// https://www.hackerrank.com/challenges/save-the-prisoner/problem

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        long q = scn.nextLong();
        for (long i = 0; i<q; i++){
            
            long n = scn.nextLong();
            long m = scn.nextLong();
            long s = scn.nextLong();
        
            m = m % n;
            
            long x = s + m - 1;
            
            if (x > n) System.out.println((s + m - 1) % n);
            else if (x == 0) System.out.println(n);
            else System.out.println(x);
        
        }
    }
}
