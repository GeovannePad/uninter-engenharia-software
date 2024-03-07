package com.empresa;

public class Livro {
    protected String titulo;
    protected Autor autor;
    protected String genero;
    protected int edicao;

    public Livro() {}

    public Livro(String titulo, Autor autor, String genero, int edicao) {
        this.titulo = titulo;
        this.autor = autor;
        this.genero = genero;
        this.edicao = edicao;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public Autor getAutor() {
        return autor;
    }

    public void setAutor(Autor autor) {
        this.autor = autor;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public int getEdicao() {
        return edicao;
    }

    public void setEdicao(int edicao) {
        this.edicao = edicao;
    }

    public void info()  {
        System.out.println("Título Livro: " + getTitulo());
        System.out.println("Gênero Livro: " + getGenero());
        System.out.println("Edição: " + getEdicao());
        System.out.println("Informações Autor");
        autor.info();
        System.out.println("----------------");
    }
}
