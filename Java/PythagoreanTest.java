import java.util.Scanner;
public class PythagoreanTest {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter an integer number for legA: ");
		int legA = scanner.nextInt(); 
		System.out.print("Enter an integer number for legB: "); 
		int legB = scanner.nextInt(); 
		Pythagorean legC = new Pythagorean();
		double C = legC.calculateHypotenouse(legA, legB);
		System.out.println("The pythagoras of " + legA + " and " + legB + " is: " + C);	
	}
}