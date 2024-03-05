package com.empresa;

public class Moeda {
    private String nome;
    private double valor;

    public Moeda(String nome, double valor) {
        setNome(nome);
        setValor(valor);
    }

    public String getNome() {
        return nome;
    }
    public double getValor() {
        return valor;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setValor(double valor) {
        this.valor = valor;
    }
}
