import java.util.Scanner;
public class Main{
	public static void main(String[] agrs) {
		Scanner scanner = new Scanner(System.in);
		int n= scanner.nextInt();
		
		for(int i=0 ; n>0 ; n--) {
			System.out.println(n);
		}
		
		scanner.close();
		
	}
	}