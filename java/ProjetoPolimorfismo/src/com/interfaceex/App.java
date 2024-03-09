package com.interfaceex;

public class App {
    public static void main(String[] args) {
        Gato g1 = new Gato();
        Animal a1 = new Gato();

        a1.emitirSom();
        g1.emitirSom();

        a1.dormir();
        g1.dormir();
    }
}
