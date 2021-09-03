// 2520  is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N ?

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            long n1 = 1;
            long s = 1;
        
            for (long i = 2; i<=n; i++){
                int c = 0;
                long temp = 1;
                for(long j = 2; j*j<=i; j++){
                
                    if(i%j == 0){
                        c++;
                        break;
                    }
                }
                if(c == 0){
                
                    while(temp<=n){
                        n1 = temp;
                        temp = temp*i;
                    }
                    s = s*n1;
                }
            }   
            System.out.println(s);
        }
    }
}
