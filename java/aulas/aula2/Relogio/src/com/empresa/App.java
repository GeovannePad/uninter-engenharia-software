package com.empresa;
public class App {
    public static void main(String[] args) {   
        Horario hora1 = new Horario();
        Horario hora2 = new Horario(1, 25, 45);

        hora2.exibirHorario();

        Horario hora3 = new Horario(2);

        hora3.exibirHorario();

        Horario hora4 = new Horario(24);
    }
}
