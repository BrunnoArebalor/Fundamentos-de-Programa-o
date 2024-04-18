import java.util.Scanner;
public class Exercicio9 {
    public static void main(String[] args) {
        /*
        9) Faça um conversor de câmbio de reais/dólar/euro. O usuário deve informar inicialmente a cotação
        de cada moeda em relação ao real. Depois apresente o seguinte menu:
        1) Converter de Real para Euro
        2) Converter de Real para Dólar
        3) Converter de Euro para Dólar
        4) Converter de Euro para Real
        5) Converter de Dólar para Euro
        6) Converter de Dólar para Real
        Leia o valor a ser convertido na moeda de origem e imprima na tela a quantidade na moeda destino.
        */
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a cotação do Euro em relação ao Real: ");
        double cotacaoEuro = sc.nextDouble();

        System.out.print("Digite a cotação do Dólar em relação ao Real: ");
        double cotacaoDolar = sc.nextDouble();

        // Exibir o menu
        System.out.println("\nEscolha uma opção:");
        System.out.println("1) Converter de Real para Euro");
        System.out.println("2) Converter de Real para Dólar");
        System.out.println("3) Converter de Euro para Dólar");
        System.out.println("4) Converter de Euro para Real");
        System.out.println("5) Converter de Dólar para Euro");
        System.out.println("6) Converter de Dólar para Real");

        int opcao = sc.nextInt();

        double valor, resultado;

        switch (opcao) {
            case 1:
                System.out.print("Digite o valor em Reais: ");
                valor = sc.nextDouble();
                resultado = valor / cotacaoEuro;
                System.out.println("Valor em Euro: " + resultado);
                break;
            case 2:
                System.out.print("Digite o valor em Reais: ");
                valor = sc.nextDouble();
                resultado = valor / cotacaoDolar;
                System.out.println("Valor em Dólar: " + resultado);
                break;
            case 3:
                System.out.print("Digite o valor em Euro: ");
                valor = sc.nextDouble();
                resultado = valor * cotacaoEuro;
                System.out.println("Valor em Dólar: " + resultado);
                break;
            case 4:
                System.out.print("Digite o valor em Euro: ");
                valor = sc.nextDouble();
                resultado = valor / cotacaoEuro;
                System.out.println("Valor em Reais: " + resultado);
                break;
            case 5:
                System.out.print("Digite o valor em Dólar: ");
                valor = sc.nextDouble();
                resultado = valor / cotacaoDolar;
                System.out.println("Valor em Euro: " + resultado);
                break;
            case 6:
                System.out.print("Digite o valor em Dólar: ");
                valor = sc.nextDouble();
                resultado = valor * cotacaoDolar;
                System.out.println("Valor em Reais: " + resultado);
                break;
            default:
                System.out.println("Opção inválida!");
        }
    }
}
