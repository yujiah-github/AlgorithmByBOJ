import java.util.Scanner;
public class Main{
	public static void main(String[] agrs) {
		Scanner scanner = new Scanner(System.in);
		int n= scanner.nextInt();
		int sum = 0;
		
		for(int i=0 ; i<=n ; i++) {
			sum = sum + i;
		}
		
		System.out.print(sum);
		
		scanner.close();
		
	}
	}