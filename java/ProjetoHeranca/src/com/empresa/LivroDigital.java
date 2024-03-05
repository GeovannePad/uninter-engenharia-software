package com.empresa;

public class LivroDigital extends Livro{
    public String linkDownload;
    public int tamanhoMb;

    public LivroDigital(String titulo, String autor, String linkDownload) {
        super(titulo, autor);
        this.linkDownload = linkDownload;
    }
 
    public float tamanhoPorPagina() {
        return tamanhoMb/(float)paginas;
    }

    public float imposto() {
        return super.imposto() + 2;
    }

    public void imprimirImposto() {
        System.out.println("Imposto Livro Físico: " + super.imposto());
        System.out.println("Imposto Livro Digital: " + this.imposto());
    }
}
