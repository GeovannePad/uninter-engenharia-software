import java.util.HashSet;

public class HashSetEx {
    public static void main(String[] args) {
        HashSet<String> nomes = new HashSet<String>();
        nomes.add("Mario");
        nomes.add("Luigi");
        nomes.add("Yoshi");
        nomes.add("Mario"); // Mario já existe portanto não será adicionado
        nomes.add("Peach");

        nomes.remove("Luigi"); // remove Luigi
        System.out.println(nomes); // imprime todos os nomes

        int total = nomes.size(); // descobre total de itens
        System.out.println(total);

        if (nomes.contains("Luigi")) { // confere se existe
            System.out.println("Ele está presente");
        } else {
            System.out.println("Não está presente");
        }
    }
}
