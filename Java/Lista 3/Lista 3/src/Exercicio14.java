import java.util.Scanner;
public class Exercicio14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("O valor do plano de saúde é 300 reias para o conveniado");
        System.out.println("Quantos dependentes o conveniado vai ter?:");

        int qtdDependentes = sc.nextInt();
        double valorConvenio = 300;
        double valorDependente = 0;

        for (int i=0; i < qtdDependentes; i++) {
            System.out.println("Qual a idade do dependebte:");
            int idade = sc.nextInt();

            if (idade <= 10) {
                valorDependente += 100;
            } else if (idade >= 11 && idade <= 30) {
                valorDependente += 220;
            } else if (idade >= 31 && idade <= 60) {
                valorDependente += 395;
            } else {
                valorDependente += 480;
            }
        }
        double valorTotal = valorConvenio + valorDependente;
        System.out.println("Valor do convênio: R$" + valorTotal);
    }
}
