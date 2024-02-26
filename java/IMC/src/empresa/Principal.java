package empresa;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		int peso;
		double altura;
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Digite o seu peso: ");
		peso = teclado.nextInt();
		System.out.print("Digite a sua altura: ");
		altura = teclado.nextDouble();
		
		double imc = peso / (altura * altura);
		System.out.printf("O seu IMC: %.2f", imc);
	}

}
