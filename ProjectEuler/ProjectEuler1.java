// Q. For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.

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

          // important to use long here otherwise it will not be able to compile for big values
          // done without loop usin AP
          
            long i5 = (n-1) / 5;
            long i3 = (n-1) / 3;  
            long i15 = (n-1) / 15;
    
            long s5 = ((i5*(10 + (i5-1)*5))/2);
            long s3 = ((i3*(6 + (i3-1)*3))/2);
            long s15 = ((i15*(30 + (i15-1)*15))/2);
    
        System.out.println(s3 + s5 - s15);
    
        }
    }
}
