import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        while(true){
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            if(a+b != 0)
            System.out.println(a+b);
            else
            	break;
        }
        
        scanner.close();
    }
    
    
}