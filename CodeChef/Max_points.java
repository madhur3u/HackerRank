// https://www.codechef.com/problems/MAXPOINT

import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Scanner.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception{
		
		Scanner scn = new Scanner(System.in);
		int t = scn.nextInt();                                              // test cases
		
		for(int x = 0; x < t; x++){
		    
		    int A = scn.nextInt();                                          // A,B,C are input time to solve a type of question
		    int B = scn.nextInt();
		    int C = scn.nextInt();
		    
		    int X = scn.nextInt();                                          // X,Y,Z are marks for diff kind of questions
		    int Y = scn.nextInt();
		    int Z = scn.nextInt();
		    
		    int ans = 0;                                                    
		    
		    for (int i = 1; i <= 20; i++){
		        for (int j = 1; j <= 20; j++){                              // i, j, k will be number of questions from a section
		            for (int k = 1; k <= 20; k++){                          // bruteforce for all, 20 questions in all 3 sections
		                
		                int total_time = i*A + j*B + k*C;                   // total time by multiplying questions count by its time

		                if (total_time <= 240)                              // since we need to do questions within 240 min
		                    ans = Math.max(ans, i*X + j*Y + k*Z);           // i*X + j*Y + k*Z is the marks for particular set of questions and we need max  
		                
		            }
		        }
		    }
		    System.out.println(ans);
		}
	}
}
