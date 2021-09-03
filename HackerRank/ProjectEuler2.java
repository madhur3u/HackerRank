// Q . Sum of EVEN fibonacci numbers till N 

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
            long n = in.nextLong();
            
            long a = 0;
            long b = 1;
            long c = 0;
            long sum = 0;
            while (c <= n){
                 
                c = a + b ;
                a = b;
                b = c;
                
                if (a % 2 == 0) sum = sum + a;
            }
            System.out.println(sum);
            
        }
    }
}
