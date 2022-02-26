import java.util.Scanner;
public class Main {
    public static void main(String[] agrs){
        Scanner scanner = new Scanner(System.in);
    
    int a = scanner.nextInt();
    int b = scanner.nextInt();
    
    if(a>b)
        System.out.print(">");
    else if(a<b)
        System.out.print("<");
    else
        System.out.print("==");
    
    scanner.close();
    }
    
}