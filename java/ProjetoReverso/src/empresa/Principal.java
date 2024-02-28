package empresa;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		ArrayList<String> listaNomes = new ArrayList<String>();
		
		System.out.print("Digite a quantidade de nomes: ");
		int qtd = teclado.nextInt();
		
		for (int i = 0;i < qtd; i++) {
			String nome = teclado.next();
			listaNomes.add(nome);
		}
		
		System.out.println("Ordem normal");
		System.out.println(listaNomes);
		
		System.out.println("Ordem reversa");
		Collections.reverse(listaNomes);
		System.out.println(listaNomes);
	}

}
