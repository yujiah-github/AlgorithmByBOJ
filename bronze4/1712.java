import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();//고정 비용
        int b = scanner.nextInt();//가변 비용
        int c = scanner.nextInt();//판매 비용
        
       if((c-b) > 0)
    	   System.out.print(a/(c-b) + 1);
       else
    	   System.out.print("-1");
    	   
        scanner.close();
    }
    
    
}