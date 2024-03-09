package com.empresa;

public class App {
    public static void main(String[] args) throws Exception {
   
        Funcionario f1 = new Assalariado("Mario", 1000);
        

        /*
        Funcionario funcionarios[] = {new Assalariado("Mario", 3500), new Horista("Luigi", 100, 40.5f), new Comissionado("Yoshi", 50000, 0.05f)};
        Funcionario f;

        for (int i = 0; i < funcionarios.length; i++) {
            f = funcionarios[i];
            System.out.println(f.nome + ", salário: " + f.pagamento());
        }
        */

        /* 
        Funcionario f1 = new Assalariado("Mario", 3500);
        f1 = new Horista("Luigi", 100, 40.5f);
        */

        /* 
        Funcionario f1 = new Funcionario("Mario"); // 0x1001
        Funcionario f2 = f1; // 0x1001 - Ponteiro, mesmo espaço de memória, "f2" aponta para o mesmo enderedeço de memória. Ao instanciar "new" atribui um espaço de memória.

        System.out.println("Nome f1: " + f1.nome);
        System.out.println("Nome f2: " + f2.nome);

        System.out.println();

        f2.nome = "Luigi";

        // Ponteiro, referência. Ao criar um objeto "f1" e atribuir a um objeto "f2", "f2" vira o ponteiro de "f1", por isso muda os dois.

        System.out.println("Nome f1: " + f1.nome);
        System.out.println("Nome f2: " + f2.nome);
        */
    }
}
