import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class LocalDateEx {
    public static void main(String[] args) throws Exception {
        LocalDate dataHoje = LocalDate.now();

        System.out.println("Original: " + dataHoje);
        DateTimeFormatter formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        String dataForm = dataHoje.format(formatador);

        System.out.println("Formatado: " + dataForm);

        LocalDateTime horario = LocalDateTime.now();

        System.out.println("LocalDateTime antes: " + horario);

        DateTimeFormatter formatadorHora = DateTimeFormatter.ofPattern("HH:mm:ss");
        String horarioFormatado = horario.format(formatadorHora);

        System.out.println("LocalDateTime depois: " + horarioFormatado);
    }
}
