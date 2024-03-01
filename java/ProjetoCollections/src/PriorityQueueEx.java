import java.util.PriorityQueue;

public class PriorityQueueEx {
    public static void main(String[] args) {
        PriorityQueue<Integer> fila = new PriorityQueue<Integer>(); // criando a fila

        fila.add(10);
        fila.add(20);
        fila.add(15);

        System.out.println(fila.peek()); // imprime o elemento do topo da fila

        System.out.println(fila.poll()); // imprime e remove ao mesmo tempo o primeiro elemento

        System.out.println(fila.peek()); // imprime o elemento do topo novamente
    }
}
