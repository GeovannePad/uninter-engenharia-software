package com.empresa;

import java.util.Scanner;

public class Principal {
    public static void main(String[] args) throws Exception {
        // inicializando todas as variáveis que serão usadas
        boolean controlador = true; // variável para controlar o loop
        int opcao; // variável para armazenar a opção escolhida pelo o usuário
        double valor; // variável para armazenar o valor da moeda digitado pelo o usuário
        Scanner cmd = new Scanner(System.in); // objeto Scanner para colher as informações digitas pelo o usuário
        Cofrinho cofrinho = new Cofrinho(); // objeto cofrinho sendo instanciado para realizar as operações propostas

        while (controlador == true) {
            
            // menu principal - início
            System.out.println("COFRINHO");
            System.out.println("--------");
            System.out.println("Opções:");
            System.out.println("1 - Adicionar uma moeda");
            System.out.println("2 - Remover uma moeda");
            System.out.println("3 - Listar todas as moedas");
            System.out.println("4 - Calcular total do cofrinho em Reais");
            System.out.println("0 - Encerrar");
            System.out.print(":");
            // menu principal - fim

            opcao = cmd.nextInt();

            // switch case para realizar o desvio de fluxo e realizar a operação desejada
            switch (opcao) {

                // encerra o programa
                case 0:
                    controlador = false;
                    cmd.close();
                    break;

                // exibe o total do cofrinho em reais e encerra o programa    
                case 4:            
                    System.out.println("Total do cofrinho em Reais: " + cofrinho.totalConvertido());
                    cmd.close();
                    controlador = false;
                    break;

                // adiciona uma moeda no cofrinho
                case 1:
                    System.out.println("Escolha a moeda que deseja adicionar:");
                    System.out.println("1 - Real");
                    System.out.println("2 - Dolar");
                    System.out.println("3 - Euro");
                    System.out.println("0 - Voltar");
                    System.out.print(":");
                    opcao = cmd.nextInt();

                    System.out.print("Digite o valor da moeda que deseja adicionar: ");
                    valor = cmd.nextDouble();

                    // switch case para adicionar a moeda adequada ao cofrinho
                    switch (opcao) {
                        case 0:
                            continue;

                        // adiciona uma moeda do tipo Real
                        case 1:
                            Real r = new Real(valor);
                            cofrinho.adicionar(r);
                            break;

                        // adiciona uma moeda do tipo Dólar
                        case 2:
                            Dolar d = new Dolar(valor);
                            cofrinho.adicionar(d);
                            break;

                        // adiciona uma moeda do tipo Euro
                        case 3:
                            Euro e = new Euro(valor);
                            cofrinho.adicionar(e);
                            break;
                        
                        default:
                            System.out.println("Opcao invalida");
                            break;
                    }
                    break;

                // exclui uma moeda do cofrinho
                case 2:
                    System.out.println("Escolha a moeda que deseja remover:");
                    System.out.println("1 - Real");
                    System.out.println("2 - Dolar");
                    System.out.println("3 - Euro");
                    System.out.println("0 - Voltar");
                    System.out.print(":");
                    opcao = cmd.nextInt();

                    System.out.print("Digite o valor da moeda que deseja remover: ");
                    valor = cmd.nextDouble();

                    // switch case para determinar qual o tipo de moeda a ser excluída do cofrinho
                    switch (opcao) {
                        case 0:
                            continue;
                        // remove uma moeda do tipo Real
                        case 1:
                            cofrinho.remover("Real", valor);
                            break;
                        // remove uma moeda do tipo Dólar
                        case 2:
                            cofrinho.remover("Dolar", valor);
                            break;
                        // remove uma moeda do tipo Euro
                        case 3:
                            cofrinho.remover("Euro", valor);
                            break;
                        default:
                            System.out.println("Opcao invalida");
                            break;
                    }
                    break;
                // lista todas as moedas contidas no cofrinho
                case 3:
                    System.out.println("Lista de moedas:");
                    cofrinho.listagemMoedas();
                    break;
                default:
                    System.out.println("Opcao invalida");
                    break;
            }
        }
    }
}
