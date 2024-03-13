public class Singleton {
    public int numero = 20;
    private static Singleton instancia = null;

    private void Singleton() {
        numero = 20;
    }

    public static Singleton getInstance() {
        if (instancia == null) {
            instancia = new Singleton();
        }
        return instancia;
    }
}
