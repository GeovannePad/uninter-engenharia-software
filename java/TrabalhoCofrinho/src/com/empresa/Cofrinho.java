package com.empresa;

import java.util.ArrayList;

public class Cofrinho {    
    private ArrayList<Moeda> listaMoedas = new ArrayList<Moeda>();

    // método para adicionar uma moeda no cofrinho
    public void adicionar(Moeda moeda) {
        listaMoedas.add(moeda);
    }

    public void remover(double valor, String tipo) {
        for (Moeda moeda : listaMoedas) {
            // verifica o tipo e o valor da moeda a ser excluída, para evitar excluir moedas diferentes com o mesmo valor
            if (moeda.getClass().toString().contains(tipo) && moeda.valor == valor) {
                listaMoedas.remove(moeda);
                break;
            }
        }
    }

    // método para listar todas as moedas presentes no cofrinho
    public void listagemMoedas() {
        for (Moeda moeda : listaMoedas) {
            moeda.info();
        }
    }

    // método para converter todas as moedas para Real e retornar o valor total do cofrinho em Reais
    public double totalConvertido() {
        double totalConvertido = 0;
        for (Moeda moeda : listaMoedas) {
            totalConvertido += moeda.converter();
        }
        return totalConvertido;
    }
}
