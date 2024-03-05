package com.empresa;

public class Aluno {
    private String nome;
    private int matricula;
    private double desconto;
    private Curso curso;

    public Aluno(String nome, int matricula, double desconto, Curso curso) {
        setNome(nome);
        setMatricula(matricula);
        setDesconto(desconto);
        setCurso(curso);
    }

    public String getNome() {
        return nome;
    }
    public int getMatricula() {
        return matricula;
    }
    public double getDesconto() {
        return desconto;
    }
    public Curso getCurso() {
        return curso;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
    public void setDesconto(double desconto) {
        this.desconto = desconto;
    }
    public void setCurso(Curso curso) {
        this.curso = curso;
    }

    public void info() {
        curso.info();
        System.out.println("Nome aluno: " + nome);
        System.out.println("Matrícula aluno: " + matricula);
        System.out.println("Desconto aluno: " + desconto);
        System.out.println("Pagamento aluno: " + pagamento());
    }

    public double pagamento() {
        return curso.getMensalidade() * (1-desconto);
    }
}
