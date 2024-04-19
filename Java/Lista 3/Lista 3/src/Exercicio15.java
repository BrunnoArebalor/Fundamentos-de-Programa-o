import java.util.Scanner;
public class Exercicio15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o preço do produto: R$ ");
        double preco = scanner.nextDouble();

        System.out.println("Escolha a condição de pagamento:");
        System.out.println("1 - À vista em dinheiro (15% de desconto)");
        System.out.println("2 - À vista no cartão de crédito (10% de desconto)");
        System.out.println("3 - Em duas vezes (sem juros)");
        System.out.println("4 - Em três vezes (com juros de 10%)");
        int opcao = scanner.nextInt();

        double precoFinal = 0;

        switch (opcao) {
            case 1:
                precoFinal = preco * 0.85; // 15% de desconto
                break;
            case 2:
                precoFinal = preco * 0.90; // 10% de desconto
                break;
            case 3:
                precoFinal = preco; // sem juros
                break;
            case 4:
                precoFinal = preco * 1.10; // 10% de juros
                break;
            default:
                System.out.println("Opção inválida!");
                return; // encerra o programa
        }
        System.out.println("Total a pagar: R$ " + precoFinal);

        scanner.close();
    }
}
