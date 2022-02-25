import java.util.Scanner;
public class Main{
	public static void main(String[] agrs) {
		Scanner scanner = new Scanner(System.in);
		int n= scanner.nextInt();
		int x= scanner.nextInt();
		
		for(int i=1 ;i<=n ; i++) {
			int j= scanner.nextInt();
			if(j<x)
				System.out.println(j);
		}
		
		scanner.close();
	}
	}