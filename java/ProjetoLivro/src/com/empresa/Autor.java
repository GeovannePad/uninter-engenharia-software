package com.empresa;

public class Autor {
    private String nome;
    private String nacionalidade;
    private String email;

    public Autor() {}

    public Autor(String nome, String nacionalidade, String email) {
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.email = email;
    }

    public String getNome() {
        return nome;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public String getEmail() {
        return email;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void info() {
        System.out.println("Nome Autor: " + getNome());
        System.out.println("Nacionalidade Autor: " + getNacionalidade());
        System.out.println("E-mail Autor: " + getEmail());
    }
}
