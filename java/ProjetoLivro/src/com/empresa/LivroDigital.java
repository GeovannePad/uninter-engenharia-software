package com.empresa;

public class LivroDigital extends Livro {
    private int tamanhoDownload;
    private double tamanhoArquivo;

    public LivroDigital() {}

    public LivroDigital(String titulo, Autor autor, String genero, int edicao, int tamanhoDownload, double tamanhoArquivo) {
        super(titulo, autor, genero, edicao);
        this.tamanhoDownload = tamanhoDownload;
        this.tamanhoArquivo = tamanhoArquivo;
    }

    public int getTamanhoDownload() {
        return tamanhoDownload;
    }

    public void setTamanhoDownload(int tamanhoDownload) {
        this.tamanhoDownload = tamanhoDownload;
    }

    public double getTamanhoArquivo() {
        return tamanhoArquivo;
    }

    public void setTamanhoArquivo(double tamanhoArquivo) {
        this.tamanhoArquivo = tamanhoArquivo;
    }

    @Override
    public void info() {
        super.info();
        System.out.println("Tamanho download Livro Digital: " + getTamanhoDownload());
        System.out.println("Tamanho arquivo Livro Digital: " + getTamanhoArquivo());
        System.out.println("----------------");
    }
}
