import java.util.Scanner;
public class Main{
	public static void main(String[] agrs) {
		Scanner scanner = new Scanner(System.in);
		int j= scanner.nextInt();
		
		for(int i=0 ; i<j; i++) {
			int a = scanner.nextInt();
		    int b = scanner.nextInt();
		    System.out.println(a+b);
		}
		
		scanner.close();
		
	}
	}