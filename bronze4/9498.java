import java.util.Scanner;
public class Main{
    public static void main(String[] args){
       Scanner scanner = new Scanner(System.in);
        
        int x = scanner.nextInt();
        
         if(x>=90)
            System.out.print("A");
         else if(x>=80)
            System.out.print("B");
         else if(x>=70)
             System.out.print("C");
         else if(x>=60)
            System.out.print("D");
        else
            System.out.print("F");
  
        scanner.close();
   
    }

    
}