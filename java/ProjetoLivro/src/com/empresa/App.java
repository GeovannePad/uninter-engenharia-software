package com.empresa;

public class App {
    public static void main(String[] args) throws Exception {
        LivroDigital ld = new LivroDigital("Senhor dos Anéis", new Autor("Tolkien", "Britânico", "tolkien@email.com"),
                "Aventura", 5, 10000, 3500);

        ld.info();
    }
}
