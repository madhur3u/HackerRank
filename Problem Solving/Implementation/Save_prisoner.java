// https://www.hackerrank.com/challenges/save-the-prisoner/problem

// In this problem, we need to determine the ID of the prisoner reached after moving M-1 steps from S.
// ID of last prisoner= (M-1+S)
// Since we are moving in a circle, we need to get the modulo of this sum with N

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
            
            long x = (s + m - 1) % n;
            
            if (x == 0) x = n;
            System.out.println(x);
        }
    }
}
