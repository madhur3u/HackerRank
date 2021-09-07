// https://www.hackerrank.com/challenges/handshake/problem

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int t = scn.nextInt();
        
        for (int t1=1; t1<=t; t1++){
            int n = scn.nextInt();
            // we have to use combination nC2 will be answer
            // nC2 = n*(n-1)/2
            System.out.println((n*(n-1))/2);
        }
        
    }
}
