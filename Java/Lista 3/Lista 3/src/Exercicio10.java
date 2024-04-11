import java.util.Scanner;
import java.util.Random;
public class Exercicio10 {
    public static void main(String[] args) {
        /*
        10) Dados não precisam ser tão “quadrados”, ou cúbicos para ser mais exato. Faça um programa que
        simule dados de 4, 6, 8, 10, 12 ou 16 faces (apenas estes valores). Peça para o usuário informar no
        começo do programa quantas faces quer, para depois fazer o sorteio.
        */
        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Digite qual o dado que vc quer jogar, dado de 4, 6, 8, 10, 12 ou 16:");
        int numeroDado = sc.nextInt();

        if (numeroDado == 4) {
            int dado = random.nextInt(numeroDado);
            System.out.println(dado);
        } else if (numeroDado == 6) {
            int dado = random.nextInt(numeroDado);
            System.out.println(dado);
        } else if (numeroDado == 8) {
            int dado = random.nextInt(numeroDado);
            System.out.println(dado);
        } else if (numeroDado == 10) {
            int dado = random.nextInt(numeroDado);
            System.out.println(dado);
        } else if (numeroDado == 12) {
            int dado = random.nextInt(numeroDado);
            System.out.println(dado);
        } else if (numeroDado == 16) {
            int dado = random.nextInt(numeroDado);
            System.out.println(dado);
        } else {
            System.out.println("Valor informado inválido!");
        }


    }
}
