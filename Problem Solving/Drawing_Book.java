// https://www.hackerrank.com/challenges/drawing-book/problem

import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int p = scn.nextInt();

        if (p > n/2) {
            if (n % 2 == 0 && n - p == 1 ) System.out.println(1);
            else System.out.println((n-p)/2);
        }
        else System.out.println(p/2);

    }
}
