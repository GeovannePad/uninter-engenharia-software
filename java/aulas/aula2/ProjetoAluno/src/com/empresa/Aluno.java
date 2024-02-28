package com.empresa;

public class Aluno {
    int matricula;
    String nome;
    String cpf;

    public void info() {
        System.out.println("nome: "+ nome);
        System.out.println("matricula: " + matricula);
        System.out.println("cpf:" + cpf);
    }
}
