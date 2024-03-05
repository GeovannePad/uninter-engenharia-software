package com.empresa;

public class Curso {
    private String nome;
    private double mensalidade;

    public Curso(String nome, int mensalidade) {
        super();
        setNome(nome);
        setMensalidade(mensalidade);
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setMensalidade(double mensalidade) {
        this.mensalidade = mensalidade;
    }

    public String getNome() {
        return nome;
    }
    public double getMensalidade() {
        return mensalidade;
    }

    public void info() {
        System.out.println("Nome curso: " + nome);
        System.out.println("Mensalidade curso: " + mensalidade);
    }
}
