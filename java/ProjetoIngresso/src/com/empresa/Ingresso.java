package com.empresa;

public class Ingresso {
    String nomeEvento;
    double valor;

    public Ingresso() {}

    public Ingresso(String nomeEvento, double valor) {
        this.nomeEvento = nomeEvento;
        this.valor = valor;
    }

    public void info() {
        System.out.println("Nome Evento: " + nomeEvento);
        System.out.println("Valor Ingresso: " + valor);
    }
}
