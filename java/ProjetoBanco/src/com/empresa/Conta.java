package com.empresa;

public class Conta {
    int numero;
    String titular;
    double saldo;
    double limite;

    Conta(int numero, String titular, double saldo, double limite) {
        this.numero = numero;
        this.titular = titular;
        this.saldo = saldo;
        this.limite = limite;
    }

    boolean sacar(double valor) {
        if(valor > limite || valor > saldo || valor <= 0) {
            return false;
        }

        saldo -= valor;
        return true;
    }

    boolean depositar(double valor) {
        if (valor <= 0) {
            return false;
        }

        saldo += valor;
        return true;
    }

    boolean transferir(Conta contaDestino, double valor) {
        if (valor > saldo || valor > limite || valor <= 0) {
            return false;
        }
        
        saldo -= valor;
        contaDestino.saldo += valor;
        return true;
    }

    void info() {
        System.out.println("Nome: " + titular);
        System.out.println("Número: " + numero);
        System.out.println("Saldo: " + saldo);
        System.out.println("Limite: " + limite);
    }
}
