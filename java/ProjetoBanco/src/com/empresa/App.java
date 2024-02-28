package com.empresa;

public class App {
    public static void main(String[] args) {
        Conta c1 = new Conta(111, "Mario", 2000, 500);
        Conta c2 = new Conta(222, "Luigi", 1500, 100);

        c1.info();

        if(!c1.sacar(200)) {
            System.out.println("Problema ao sacar!");
        }

        if (!c1.depositar(-500)) {
           System.out.println("Problema ao depositar!"); 
        }

        System.out.println();
        c1.info();

        if(!c2.transferir(c1, 100)) {
            System.out.println("Problema ao transferir!");
        }

        System.out.println();
        c1.info();
        System.out.println();
        c2.info();
    }
}
