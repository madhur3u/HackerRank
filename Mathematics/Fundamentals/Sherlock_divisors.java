// https://www.hackerrank.com/challenges/sherlock-and-divisors/problem

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int q = scn.nextInt();

        for (int w =1; w<=q; w++){
            long n = scn.nextLong();
            int c = 1;                             // c is one as we are not taking last no. which will be divided by 2 for even
            if (n % 2 != 0) System.out.println(0); // will be zero if no. is odd
            else{
                for (int i = 2; i*i<=n; i++){            // checking all divisor till sqrt n
                    if(n % i == 0 && i % 2 == 0)c++;
                        
                    if(n%(n/i)==0 && (n/i != i) && (n/i)%2==0) c++;  // checking all divisor from end to sqrt n and including sqrt 1 here using (n/i != i)
                }
                System.out.println(c);
            }
            
            
        }

    }
}
