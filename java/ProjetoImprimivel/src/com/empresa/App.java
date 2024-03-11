package com.empresa;

import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        Funcionario f = new Funcionario("Mario", "111.222.333-44");
        Carro c = new Carro("Palio", "Cinza", 4);
        Quadrado q = new Quadrado(10);

        ArrayList<Imprimivel> imprimiveis = new ArrayList<Imprimivel>();

        imprimiveis.add(f);
        imprimiveis.add(c);
        imprimiveis.add(q);

        for (Imprimivel i : imprimiveis) {
            i.imprimir();
        }
    }
}
