package empresa;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		int numero_soldados;
		String msg;
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.print("Insira a quantia de soldados que Leonidas vai enfrentar: ");
		numero_soldados = teclado.nextInt();
		
		while (numero_soldados != 10000) {
			
			msg = numero_soldados > 10000 ? "Um pouco menos" : "Um pouco mais";
			System.out.println(msg);
			
			/*if (numero_soldados > 10000) {
				System.out.println("Errou, um poucos menos");
			} else if (numero_soldados < 10000) {
				System.out.println("Errou, um pouco mais");
			}*/
			
			System.out.print("Insira a quantia de soldados novamente: ");
			numero_soldados = teclado.nextInt();
		}
		System.out.println("Acertou, parabens");
	}

}
