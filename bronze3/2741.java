import java.util.Scanner;
public class Main{
	public static void main(String[] agrs) {
		Scanner scanner = new Scanner(System.in);
		int n= scanner.nextInt();
		
		for(int i=1 ; i<=n ; i++) {
			System.out.println(i);
		}
		
		scanner.close();
		
	}
	}