package com.empresa;

public class Conta {
    String correntista;
    double saldo;
    double limiteSaque;

    public void info() {
        System.out.println("nome correntista: " + correntista);
        System.out.println("saldo: " + saldo);
        System.out.println("limite de saque: " +limiteSaque);
    }

    public void sacar(double valor) {
        if (valor > limiteSaque || valor > saldo) {
            System.out.println("saque não permitido");
        } else {
            saldo -= valor;
        } 
    }

    public void depositar(double valor) {
        saldo += valor;
    }

    public void transferir(Conta conta_destino, double valor) {
        if (valor > saldo || valor > limiteSaque) {
            System.out.println("transferência não permitida");
        } else {
            saldo -= valor;
            conta_destino.saldo += valor;
        }
    }
}
