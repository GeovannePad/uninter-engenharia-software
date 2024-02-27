package com.empresa;
public class App {
    public static void main(String[] args) throws Exception {
        Conta correntistaA = new Conta();

        correntistaA.correntista = "1001";
        correntistaA.saldo = 100.50;
        correntistaA.limiteSaque = 100;

        Conta correntistaB = new Conta();

        correntistaB.correntista = "1002";
        correntistaB.saldo = 10000.50;
        correntistaB.limiteSaque = 1000;

        correntistaA.info();

        correntistaA.sacar(10.50);
        correntistaB.sacar(1000.50);

        correntistaA.info();
        correntistaB.info();

        correntistaA.depositar(100000);
        correntistaB.transferir(correntistaA, 1000);

        correntistaA.info();
        correntistaB.info();
    }
}
