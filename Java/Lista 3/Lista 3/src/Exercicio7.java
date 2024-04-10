import java.util.Scanner;

public class Exercicio7 {
    public static void main(String[] args) {
        /*
        7) Implementar um programa que calcula o desconto previdenciário de um funcionário. O programa
        deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto
        segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é
        318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20.
        */
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite o seu salário para ver o desconto que vc vai ter:");
        double salario = sc.nextDouble();
        double descontoSalario = (salario * 11) / 100;
        double tetoMaximo = 318.20;

        if (descontoSalario < tetoMaximo) {
            double salarioFinal = salario - descontoSalario;
            System.out.printf("Salário com descontos ficou: R$%.2f", salarioFinal);
        }
        else {
            double salarioFinal = salario - tetoMaximo;
            System.out.printf("Salário com desconto ficou: R$%.2f", salarioFinal);
        }
    }
}
