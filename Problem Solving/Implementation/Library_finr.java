// https://www.hackerrank.com/challenges/library-fine/problem

    import java.io.*;
    import java.util.*;

    public class Solution {
        public static void main(String[] args) {

            Scanner scn = new Scanner(System.in);
            int d1 = scn.nextInt();
            int m1 = scn.nextInt();
            int y1 = scn.nextInt();
            int d2 = scn.nextInt();
            int m2 = scn.nextInt();
            int y2 = scn.nextInt();

            if(y1 - y2 > 0) System.out.println(10000);
            else if (y1 == y2 && m1 - m2 > 0) System.out.println(500*(m1-m2));
            else if (y1 == y2 && m1 == m2 && d1 - d2 > 0) System.out.println(15*(d1-d2));
            else System.out.println(0);
        }
    }
