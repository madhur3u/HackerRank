// https://www.hackerrank.com/challenges/electronics-shop/problem

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        String[] bnm = scn.nextLine().split(" ");
        int b = Integer.parseInt(bnm[0]);
        int n = Integer.parseInt(bnm[1]);
        int m = Integer.parseInt(bnm[2]);
        String[] kb = scn.nextLine().split(" ");
        String[] usb = scn.nextLine().split(" "); // input ends here
        
        // Integer.parseInt(kb[1])
        int max = -1;
        for (int i = 0; i<n; i++){

            if (Integer.parseInt(kb[i]) < b){
                for (int j = 0; j<m; j++){

                    int t = Integer.parseInt(kb[i]) + Integer.parseInt(usb[j]);
                    if(t > max && t <= b) max = t;

                }
            }
        }
        System.out.println(max);
    }
}

// see discussion for better O(n)
