// https://www.hackerrank.com/challenges/halloween-party/problem

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        long q = scn.nextLong();
        
        for (long i = 1; i<=q; i++){
            long n = scn.nextLong();
            
            if(n%2==0) {
                long ans = (n/2)*(n/2);             // formula for even
                System.out.println(ans);
            }
            else{
                long ans = ((n+1)/2)*((n+1)/2 - 1); // formula for odd
                System.out.println(ans);
            }
        }
    }
}
/*     k=input()
       print (k/2)*(k-k/2)      */
