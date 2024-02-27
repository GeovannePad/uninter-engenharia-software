package com.empresa;

public class App {
    public static void main(String[] args) throws Exception {
        Aluno mario = new Aluno();
        mario.cpf = "111.111.111-11";
        mario.nome = "Super Mario";
        mario.matricula = 1001;

        Aluno luigi = new Aluno();
        luigi.cpf = "222.222.222-22";
        luigi.nome = "Super Luigi";
        luigi.matricula = 1002;

        Aluno yoshi = new Aluno();

        yoshi.cpf = "333.333.333-33";
        yoshi.nome = "Super Yoshi";
        yoshi.matricula = 1003;

        Aluno antigo;

        if (mario.matricula < luigi.matricula) {
            if (mario.matricula < yoshi.matricula) {
                antigo = mario;
            } else {
                antigo = yoshi;
            }
        } else {
            if (luigi.matricula < yoshi.matricula) {
                antigo = luigi;
            } else {
                antigo = yoshi;
            }
        }

        System.out.println("Aluno mais antigo ");
        antigo.info();
    }
}
