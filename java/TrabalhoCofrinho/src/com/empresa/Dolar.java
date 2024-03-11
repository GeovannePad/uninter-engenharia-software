package com.empresa;

public class Dolar extends Moeda {

    public Dolar(double valor) {
        super(valor);
    }

    // método para exibir a informação da moeda Dólar em questão
    @Override
    public void info() {
        System.out.println("Dólar: " + super.valor);
    }

    // o valor usado para converter a moeda Dólar para Real foi de R$ 5,00.
    @Override
    public double converter() {
        return valor * 5.00;
    }

}
