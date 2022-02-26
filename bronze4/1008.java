import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        double a = scanner.nextInt();
        double b = scanner.nextInt();
        double sum = a / b;
        
        System.out.println(sum);
        
        scanner.close();
    }
}