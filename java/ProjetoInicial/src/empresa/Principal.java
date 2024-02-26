package empresa;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		int idade = 10;
		
		double peso = 72.5;
		String nome = "Mario";
		float peso2 = 80.6f;
		
		idade = idade + 2;
		
		System.out.println("Idade: " + idade);
		System.out.printf("Idade: %d\n", idade);
		System.out.printf("Peso: %.2f\n", peso);
		
		Scanner dado = new Scanner(System.in);
		
		System.out.println("Digite idade, peso e nome");
		
		idade = dado.nextInt();
		peso = dado.nextDouble();
		nome = dado.next();
		
		System.out.println("Nome: " + nome);
		System.out.println("Idade: " + idade);
		System.out.printf("Peso: %.2f\n", peso);
		
		if (idade < 18) {
			System.out.println("Acesso bloqueado");
		} else if (idade < 65) {
			System.out.println("Adulto");
		} else {
			System.out.println("Adulto idoso");
		}
		
		for(int i = 0;i < 10; i += 1) {
			System.out.println("Valor: " + i);
		}
		
		int megaSena[] = {11,14,21,30,37,56};
		int numeros[] = new int[200];
		
		megaSena[1] = 10;

	}

}
