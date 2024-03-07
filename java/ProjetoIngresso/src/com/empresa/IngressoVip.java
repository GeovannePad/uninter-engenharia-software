package com.empresa;

public class IngressoVip extends Ingresso {
    double valorAdicional;

    public IngressoVip() {}

    public IngressoVip(String nomeEvento, double valor, double valorAdicional) {
        super(nomeEvento, valor);
        this.valorAdicional = valorAdicional;
    }

    @Override
    public void info() {
        super.info();
        System.out.println("Valor Adicional" + valorAdicional);
        System.out.println("Total Ingresso VIP: " + (super.valor + valorAdicional));
        System.out.println("----------");
    }
}
