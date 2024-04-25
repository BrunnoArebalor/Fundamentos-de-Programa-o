import java.util.Scanner;
public class Exercicio2 {
    public static void main(String[] args) {
        System.out.println("2. (3.0 pts) Agora crie uma função divisivelPorN que receba como parâmetro dois números inteiros e retorne\n" +
                "True se o primeiro é divisível pelo segundo, e False caso contrário. O segundo parâmetro não pode ser zero,\n" +
                "então cheque isso dentro da função (se for zero, imprima uma mensagem dizendo que não é possível efetuar\n" +
                "divisão por zero e retorne False).");

        Scanner sc = new Scanner(System.in);
        System.out.println("Digite dois valores para ver se o primeiro é divisivel pelo segundo:");
        int divisivelPorN1 = sc.nextInt();
        int divisivelPorN2 = sc.nextInt();

        if (divisivelPorN1 % divisivelPorN2 == 0 && divisivelPorN2 != 0) {
            System.out.println("Primeiro valor " + divisivelPorN1 + " divisível por " + divisivelPorN2);
            System.out.println("Valor verdadeiro");
        } else if (divisivelPorN2 == 0) {
            System.out.println("Não é possível efetuar uma divisão por ZERO!");
            System.out.println("FALSO!");
        } else {
            System.out.println("Primeiro valor " + divisivelPorN1 + " não é divisível por " + divisivelPorN2);
            System.out.println("FALSO!");
        }

    }
}
