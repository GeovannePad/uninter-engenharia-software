public class Conta {
    String nome;
    double saldo;

    public Conta(String nome, double saldo) {
        this.nome = nome;
        this.saldo = saldo;
    }

    public void depositar(double valor) {
        if (valor <= 0) {
            throw new RuntimeException("Valor invalido");
        }
        saldo += valor;
    }

    public void sacar(double valor) throws Exception {
        if (valor > saldo) {
            throw new Exception("Saldo insuficiente");
        }
        if (valor <= 0) {
            throw new Exception("Valor invalido");
        }
        saldo -= valor;
    }

    public void transferir(double valor, Conta destino) throws Exception {
        this.sacar(valor);
        destino.saldo += valor;
    }

    public void info() {
        System.out.println("-----------");
        System.out.println("Nome: " + nome);
        System.out.println("Saldo: " + saldo);
    }
}
