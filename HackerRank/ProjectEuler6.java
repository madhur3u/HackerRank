// Q. (1+2+3+...+n)^2 - (1^2 + 2^2 +3^2 +...+ n^2)

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
            long n = in.nextInt();
        
            long s1 = (n*(n+1))/2;
            long s2 = (n*(n+1)*(2*n+1))/6;
        
            System.out.println(s1*s1 - s2);
        }
    }
}
