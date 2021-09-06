// https://www.hackerrank.com/challenges/drawing-book/problem

import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int p = scn.nextInt();

       /* if (p > n/2) System.out.println((n/2) - (p/2));
        else System.out.println(p/2); */

        System.out.println((int)Math.min(((n/2) - (p/2)) , (p/2)));  // solve in one line by finding minimum
    }
}

