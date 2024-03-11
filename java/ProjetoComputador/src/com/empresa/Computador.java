package com.empresa;

public abstract class Computador {
    int gbMemoria, numProcessadores;

    public Computador(int gbMemoria, int numProcessadores) {
        this.gbMemoria = gbMemoria;
        this.numProcessadores = numProcessadores;
    }

    public abstract double calculaValor();
}
