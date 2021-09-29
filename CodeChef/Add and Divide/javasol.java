// https://www.codechef.com/problems/ADDNDIV

import java.util.*;

public class test {

    public static void main(String[] args) throws Exception 
    {
        Scanner scn = new Scanner(System.in);
        int t = scn.nextInt();

        for (int t0 = 0; t0<t; t0++)
        {                                               // no. of testcases
            int a = scn.nextInt();
            int b = scn.nextInt();

            int gcd = GCD(a, b);

            while (gcd != 1)
            {
                a = a / gcd;
                gcd = GCD(a, b);
            }

            if (a == 1) System.out.println("YES");
            else        System.out.println("NO");
    

        }
    }
    public static int GCD(int x, int y) 
    {
        int temp;
        while (y > 0)
        {
            temp = y;
            y = x % y;
            x = temp;
        }    
        return x;
    }
}
