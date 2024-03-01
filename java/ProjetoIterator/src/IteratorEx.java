import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.ListIterator;

public class IteratorEx {
    public static void main(String[] args) throws Exception {
        ArrayList<Integer> lista = new ArrayList<Integer>();
        HashSet<Integer> conjunto = new HashSet<Integer>();
        HashMap<String,Integer> mapa = new HashMap<String,Integer>();

        int soma;

        soma = 0;
        // For simples
        for (int i = 0; i < lista.size(); i++) {
            soma += lista.get(i);
        }

        soma = 0 ;;
        // For each
        for (int item : lista) {
            
        }

        soma = 0;
        // Iterator
        //Iterator it = mapa.entrySet().iterator();
        //Iterator it = conjunto.iterator();
        //Iterator it = lista.iterator();

        //while (it.hasNext()) {
           //soma += (int)it.next(); 
        //}

        // Suponha lista como um ArrayList com dados de algum tipo, por exemplo strings.
        //ListIterator it = lista.listIterator(lista.size());
        
        //while (it.hasPrevious()) {
            //System.out.println(it.previous());
        //}

        
    }
}
