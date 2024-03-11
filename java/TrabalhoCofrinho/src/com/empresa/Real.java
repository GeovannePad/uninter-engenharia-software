package com.empresa;

public class Real extends Moeda{

    public Real(double valor) {
        super(valor);
    }

    // método para exibir a informação da moeda Real em questão
    @Override
    public void info() {
        System.out.println("Real: " + super.valor);
    }

    // método para converter a moeda Real para Real.
    @Override
    public double converter() {
        return valor;
    }
    
}
