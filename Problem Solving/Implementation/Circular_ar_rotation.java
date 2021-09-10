// https://www.hackerrank.com/challenges/circular-array-rotation/problem

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int k = scn.nextInt();
        int q = scn.nextInt();
        int[] a = new int[n];
        int[] b = new int[n];
        for (int i = 0; i < n; i++){
            a[i] = scn.nextInt();      // input array
        }
        k = k % n; // for k>n
        k = n - k; // the logic below is for left rottion so doing this convert it to right rotation 
        for (int i = 0; i < n; i++){
            b[i] = a[(i+k)%n];
        }
        for (int i = 0; i < q; i++){
            int q1 = scn.nextInt();
            System.out.println(b[q1]);
        }

    }
}

/* ALT BETTER PYTHON CODE

n, k, q = map(int, input().split())
a = list(map(int, input().split()))
    
for i in range(q):
    q1 = int(input())
    print(a[(q1 - k) % n])   */
