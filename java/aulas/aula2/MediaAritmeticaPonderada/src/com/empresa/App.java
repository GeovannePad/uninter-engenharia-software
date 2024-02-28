package com.empresa;

public class App {
    public static void main(String[] args) {
        double media;

        Nota calculo = new Nota();

        calculo.nota1 = 2.5;
        calculo.nota2 = 2.0;
        calculo.nota3 = 1.5;

        media = calculo.calcularMediaAritmetica();
        System.out.printf("Média Aritmética: %.2f\n", media);

        media = calculo.calcularMediaPonderada();
        System.out.printf("Média Ponderada: %.2f\n", media);

    }

}
