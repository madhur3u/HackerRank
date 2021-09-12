// https://www.hackerrank.com/challenges/sherlock-and-squares/problem

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int q = scn.nextInt();

        for (int q1 = 1; q1<=q; q1++){

            int a = scn.nextInt();
            int b = scn.nextInt();
            int a1 = (int)Math.sqrt(a);
            int b1 = (int)Math.sqrt(b);
            int i = a1;

        //    for (i = i ; i <= b1; i++) System.out.println(i*i);  //to print squares in that range
            int c = b1 - a1;
            if (a == a1*a1) c++;

            System.out.println(c);

        }
    }
}

/* alt python code 

import math
t = input()
for _ in range(t):
    a, b = map(int, input().split())
    a = ceil(sqrt(a))
    b = floor(sqrt(b))
    print int(b-a) + 1
*/
