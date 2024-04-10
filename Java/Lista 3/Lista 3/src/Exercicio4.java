import java.util.Scanner;
public class Exercicio4 {
    public static void main(String[] args) {
        /*
        4) Crie um programa que verifica se um número inteiro informado pelo usuário é divisível por 3.
        */
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um numero para ver se ele é divisivel por 3:");
        int numero = sc.nextInt();

        if (numero % 3 == 0) {
            System.out.println("Esse valor é divisivel por 3");
        }
        else {
            System.out.println("Esse valor não é divisivel por 3");
        }
    }
}
