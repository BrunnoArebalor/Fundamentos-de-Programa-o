import java.util.Scanner;
public class Exercicio5 {
    public static void main(String[] args) {
        /*
        5) Faça um algoritmo para receber um número qualquer do usuário e informar na tela se é par ou se é ímpar.
        */
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite um valor para ver se é par ou impar:");
        int numero = sc.nextInt();

        if (numero % 2 == 0) {
            System.out.println("O número " + numero + " é PAR!");
        }
        else {
            System.out.println("O número " + numero + " é IMPAR!");
        }
    }
}
