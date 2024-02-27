package com.empresa;

public class Nota {
    double nota1, nota2, nota3;

    public double calcularMediaAritmetica() {
        double media = (nota1 + nota2 + nota3) / 3;
        return media;
    }

    public double calcularMediaPonderada() {
        double media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4)) / 9;
        return media;
    }
}
