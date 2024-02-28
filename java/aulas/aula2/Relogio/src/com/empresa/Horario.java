package com.empresa;
public class Horario {
    int hora, minuto, segundo;

    Horario(int hora, int minuto, int segundo) {
        if(!(hora >= 0 && hora < 24)) {
            this.hora = 0;
            System.out.println("Erro nas horas, iniciando com o valor zero.");
        } else if (!(minuto >= 0 && minuto < 60)) {
            this.minuto = 0;
            System.out.println("Erro nos minutos, iniciando com o valor zero.");
        } else if (!(minuto >= 0 && minuto < 60)) {
            this.segundo = 0;
            System.out.println("Erro nos segundos, iniciando com o valor zero.");
        } else {
            this.hora = hora;
            this.minuto = minuto;
            this.segundo = segundo;
        }
    }

    Horario(int hora) {
        if(!(hora >= 0 && hora < 24)) {
            this.hora = 0;
            System.out.println("Erro nas horas, iniciando com o valor zero.");
        } else {
            this.hora = hora;
        }
    }

    Horario() {
        System.out.println("Construtor sem parâmetros");
    }

    public void exibirHorario() {
        System.out.println("Horário: " + hora + ":" + minuto + ":" + segundo);
    }
}
