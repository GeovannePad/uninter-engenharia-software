package com.empresa;

public class Quadrado implements Imprimivel{
    int medidaLado;

    public Quadrado(int medidaLado) {
        this.medidaLado = medidaLado;
    }

    @Override
    public void imprimir() {
        System.out.println("Quadrado");
        System.out.println("Medida lado: " + medidaLado);
        System.out.println("Area: " + (medidaLado *  medidaLado));
        System.out.println("----------");
    }
}
