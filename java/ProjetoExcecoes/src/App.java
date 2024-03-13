import java.util.Scanner;

public class App {
    public static void funcao() {
		try {
			throw new NullPointerException("Problema!");
		} catch(NullPointerException e) {
			System.out.println("funcao(): " + e);
			throw e;
		}
	}

    public static void main(String[] args) throws Exception {
        int[] numeros = {1,2,3};

        try {
            numeros[0] = numeros [0] / 0;
            System.out.println(numeros[10]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Fora do limite");
        } catch (Exception e) {
            System.out.println("Ocorreu um problema: " + e.getMessage());
        } finally {
            System.out.println("Finalizando programa");
        }

        System.out.println("Digite um valor entre 0 e 10");
        Scanner teclado = new Scanner(System.in);
        int valor = teclado.nextInt();

        if (valor > 10 || valor < 0) {
            throw new RuntimeException("Valor Inválido");
        }

        try {
			funcao();
		} catch(NullPointerException e) {
			System.out.println("main(): " + e);
		}

        String s1 = new String("MSG"); // 0x1001
        String s2 = new String("MSG"); // 0x1002
        String s3 = s1; // 0x1001

        System.out.println(s1 == s2);
        System.out.println(s1 == s3);

        System.out.println(s1.equals(s2));
        System.out.println(s1.equals(s3));

        System.out.println("---------");

        Usuario u1 = new Usuario(111, "Mario", "111.222.333-44");
        Usuario u2 = new Usuario(111, "Mario", "111.222.333-44");
        Usuario u3 = u1;

        System.out.println(u1 == u2);
        System.out.println(u1 == u3);

        System.out.println(u1.equals(u2));
        System.out.println(u1.equals(u3));

        System.out.println(u1);

        Singleton sin1 = Singleton.getInstance();
        Singleton sin2 = Singleton.getInstance();

        sin1.numero += 10;
        System.out.println(sin1.numero);
        System.out.println(sin2.numero);
    }
}
