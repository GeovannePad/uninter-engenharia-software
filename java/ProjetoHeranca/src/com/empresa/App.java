package com.empresa;

public class App {
    public static void main(String[] args) {
        Livro l1 = new Livro("Como", "Giovanni");
        l1.imposto();

        LivroDigital l2 = new LivroDigital("Por que", "Beatriz", "link do site");
        System.out.println(l1 instanceof Livro);
        System.out.println(l2 instanceof Livro);

        System.out.println(l1 instanceof LivroDigital);
        System.out.println(l2 instanceof LivroDigital);
    }
}
