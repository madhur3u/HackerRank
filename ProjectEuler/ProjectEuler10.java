// Q. Print sum of all prime no. till N
// if N = 10 print 2+3+5+7 = 17

public class HelloWorld{

     public static void main(String []args){
        System.out.println("Hello World");
        
        long n = 100000;
        long s = 0;
        if (n >= 2) s = 2;
        for (long i = 3; i<=n; i+=2){
            int c = 0;
            long temp = 1;
            for(long j = 2; j*j<=i; j++){
                
                if(i%j == 0){
                    c++;
                    break;
                }
            }
            if(c == 0){
                
                s = s+i;
            }
        }
        System.out.println(s);
        
        
     }
}
