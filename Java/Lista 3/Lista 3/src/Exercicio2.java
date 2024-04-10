import java.util.Scanner;
public class Exercicio2 {
    public static void main(String[] args){
        /*
        2) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A
        + C.
        */
        Scanner sc = new Scanner(System.in);

        float A = sc.nextFloat();
        float B = sc.nextFloat();
        float C = sc.nextFloat();

        float soma1 = A + B;
        float soma2 = A + C;

        if (soma1 > soma2) {
            System.out.println("Soma de A+B maior que soma de A+C");
        }
        else {
            System.out.println("Soma de A+B menor que soma de A+C");
        }
    }
}
