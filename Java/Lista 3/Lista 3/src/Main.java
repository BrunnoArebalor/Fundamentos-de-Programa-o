import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        /*
        1) Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for
        diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.
         */
        Scanner sc = new Scanner(System.in);
            float numero1 = sc.nextFloat();
            float numero2 = sc.nextFloat();

            if (numero1 != 0 && numero2 != 0) {
                float resultado = numero1 / numero2;
                System.out.println("resultado:" + resultado);
            }
            else {
            System.out.println("Valor invalido para divisão!");
        }

    }
}