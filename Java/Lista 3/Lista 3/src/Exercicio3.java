import java.util.Scanner;
public class Exercicio3 {
    public static void main(String[] args) {
        /*
        3) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo
        o resultado.
        */
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um número, se ele for positivo vai duplicar o valor" +
                "se for negativo vai triplicar");
        int numero = sc.nextInt();
        if (numero > 0) {
            int dobro = numero * 2;
            System.out.println("O dobro do valor digitado" + numero + "é: " + dobro);
        }
        else {
            int tripulo = numero * 2;
            System.out.println("O tripulo do valor digitado" + numero + "é: " + tripulo);
        }
    }
}
