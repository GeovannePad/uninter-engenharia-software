import java.util.ArrayList;
import java.util.LinkedList;

public class ArrayListLinkedListEx {
    public static void main(String[] args) throws Exception {
        
        ArrayList<String> pessoas = new ArrayList<String>();
        //LinkedList<String> pessoas = new LinkedList<String>();

        pessoas.add("Mario"); // adição de novos elementos
        pessoas.add("Luigi");
        pessoas.add("Peach");
        pessoas.add("Yoshi");

        System.out.println(pessoas); // lista dos elementos

        String item1 = pessoas.get(0); // retorna o elemento de índice 0
        System.out.println(item1);

        pessoas.remove(3); // remove o elemento de índice 3

        int total = pessoas.size(); // retorna a quantidade de elementos
        System.out.println(total);

        pessoas.clear(); // remove todos os elementos

    }
}
