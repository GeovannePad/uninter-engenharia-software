package com.empresa;

public class Euro extends Moeda{

    public Euro(double valor) {
        super(valor);
    }

    // método para exibir a informação da moeda Euro em questão
    @Override
    public void info() {
        System.out.println("Euro: " + super.valor);
    }

    // o valor usado para converter a moeda Euro para Real foi de R$ 5,50.
    @Override
    public double converter() {
        return valor * 5.50;
    }

}
