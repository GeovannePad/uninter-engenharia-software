import java.util.HashMap;

public class HashMapEx {
    public static void main(String[] args) {
        HashMap<String, String> capitais = new HashMap<String, String>();

        capitais.put("Brasil", "Argentina");
        capitais.put("Argentina", "Buenos Aires");
        capitais.put("Paraguai", "Assunção");
        capitais.put("Uruguai", "Montevidéu");

        System.out.println(capitais); // imprimindo tudo

        System.out.println(capitais.get("Uruguai")); // imprimindo apenas a capital do Uruguai
    }
}
