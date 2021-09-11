// https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import java.io.*;
import java.math.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner scn = new Scanner(System.in);
        int[][] a = new int[6][6];
        for(int i = 0; i<6; i++){
            for (int j = 0; j<6; j++){
                a[i][j] = scn.nextInt();
            }
        }
        int max = -100;
        for(int i = 0; i<4; i++){
            for (int j = 0; j<4; j++){
              int s =(a[i][j]+a[i][j+1]+a[i][j+2]) + (a[i+1][j+1]) + (a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]);
              max = Math.max(max, s);
            }
            
        }
        System.out.println(max);
    }
}
