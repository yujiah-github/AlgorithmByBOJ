import java.util.Scanner;
public class Main{
    public static void main(String[] agrs){
        Scanner scanner = new Scanner(System.in);
        
        int x = scanner.nextInt();
        if(x%4 == 0)
        {
            if((x%100 != 0) || (x%400 == 0))
                System.out.print("1");
            else
                System.out.print("0");
        }
        else
            System.out.print("0");
        
        
        scanner.close();
    }
    
    
}