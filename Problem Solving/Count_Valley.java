// https://www.hackerrank.com/challenges/counting-valleys/problem

import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = Integer.parseInt(scn.nextLine());
        String st = scn.nextLine();

        int l = 0;
        int v = 0;

        for (int i = 0; i<n ; i++){

            int c = l;
            if (st.charAt(i) == 'U') l++;
            else l--;

            if (c == 0 && l == -1) v++;
        }
        System.out.println(v);
       
    }
}
