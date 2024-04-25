import java.util.Scanner;
public class Exercicio1 {
    public static void main(String[] args) {
        System.out.println("1. (2.0 pts) Faça uma função divisivelPor2 que receba como parâmetro um número inteiro, e retorne True se o\n" +
                "número é divisível por 2, e False caso contrário.");

        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um valor para o programa ver se esse número é divisível por 2:");
        double divisivelPor2 = sc.nextDouble();

        if (divisivelPor2 % 2 == 0) {
            System.out.println("Valor informado é verdadeiro!");
            System.out.println("Valor informado:" + divisivelPor2);
        } else {
            System.out.println("Valor informado é falso!");
            System.out.println("Valor informado:" + divisivelPor2);
        }
    }
}
