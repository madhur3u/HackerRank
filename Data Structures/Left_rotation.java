/* https://www.hackerrank.com/challenges/array-left-rotation/problem
Sample Input
5 4
1 2 3 4 5
Sample Output
5 1 2 3 4
*/


import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int k = scn.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++){
            a[i] = scn.nextInt();      // input array
        }

        for (int i = 0; i < n; i++){
            System.out.print(a[(i+k)%n] + " ");
        }

    }
}

/* PYTHON PROGRAM 
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in a[k:n] : print(i, end=' ')
for j in a[0:k] : print(j, end=' ')
*/
