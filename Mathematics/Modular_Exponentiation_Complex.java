import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        Long n = scn.nextLong();
        
        for (int i =1; i<=n; i++){
            Long a = scn.nextLong();
            Long b = scn.nextLong();
            Long y = scn.nextLong();
            Long m = scn.nextLong();

            // to find ((a+ib)**y)%m
            // RUSSIAN PEASENT EXPONENTIATION METHOD IN COMPLEX

            long c = 1;
            long d = 0; // this will be our result initial value 1 + 0i
            while (y > 0) {

                if (y % 2 != 0){ // for y odd we will update res
                    // (a + bi) * (c + di) = (ac - bd) + i(ad + bc)

                    long t1 = ((a*c)%m - (b*d)%m + m)%m  ;   // if y odd then multiply res by x since 
                    d = ((a*d)%m + (b*c)%m)%m  ;
                    c = t1;       
                }
                y = y/2;
                long t = ((a*a)%m - (b*b)%m + m)%m ;    // x * x at each step complex
                b = ((a*b)%m + (b*a)%m)%m ;
                a = t;
            }

            System.out.println(c +" "+d);
        }

    }
}
