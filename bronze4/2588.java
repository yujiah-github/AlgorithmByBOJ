import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c1= (b/100); //100의 자리 수
        int c2= ((b/10)-(c1*10)); //10의 자리 수
        int c3= b - ((c1*100) + (c2 *10)); //1의 자리 수
        int sum1 = (a * c3) ; //첫 번째 합계
        int sum2 = (a * (c2*10)); // 두 번째 합계
        int sum3 = (a * (c1*100)); //세 번째 합계
        int allsum = sum1 + sum2 +sum3;
        int sum2_print = (sum2 /10);
        int sum3_print = (sum3/100);
        
        System.out.println(sum1);
        System.out.println(sum2_print);
        System.out.println(sum3_print);
        System.out.println(allsum);
        
        
        scanner.close();
        
        
        
    }
      
}