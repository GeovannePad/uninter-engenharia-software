package com.empresa;

public class Aritmetica {
    static public void somar(double a, double b) {
        double resultado;
        resultado = a + b;

        System.out.printf("Resultado da soma: %.2f\n", resultado);
    }

    static public void subtrair(double a, double b) {
        double resultado;
        resultado = a - b;

        System.out.printf("Resultado da subtração: %.2f\n", resultado);
    }

    static public void multiplicar(double a, double b) {
        double resultado;
        resultado = a * b;

        System.out.printf("Resultado da multiplicação: %.2f\n", resultado);
    }

    static public void dividir(double a, double b) {
        double resultado;

        if (b == 0) {
            System.out.println("Impossível dividir por zero.");
        } else {
            resultado = a / b;
            System.out.printf("Resultado da divisão: %.2f\n", resultado);
        }
    }
}
