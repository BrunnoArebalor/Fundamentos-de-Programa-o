import java.util.Scanner;
public class Exercicio13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite a sua nota do grau A");
        double grauA = sc.nextDouble();
        System.out.println("Digite a sua nota do grau B");
        double grauB = sc.nextDouble();
        double primeiraMedia = (grauA + (grauB * 2)) / 3;

        if (primeiraMedia < 6) {
            System.out.println("Estudante ficou abaixo da media!");
            System.out.println("Estudante quer recuperar o Grau A ou B?:");
            String recuperar = sc.next();
            if (recuperar == "A"){
                System.out.println("Qual a nova nota:");
                double segundoGrauA = sc.nextDouble();
                double segundaMedia = (segundoGrauA + (grauB * 2)) / 3;
                if (segundaMedia < 6) {
                    System.out.println("Reprovado!");
                    System.out.println("Média: " + segundaMedia);
                } else {
                    System.out.println("Aprovado!");
                    System.out.println("Média: " + segundaMedia);
                }
            } else {
                System.out.println("Qual a nova nota:");
                double segundoGrauB = sc.nextDouble();
                double segundaMedia = (grauA + (segundoGrauB * 2)) / 3;
                if (segundaMedia < 6) {
                    System.out.println("Reprovado!");
                    System.out.println("Média: " + segundaMedia);
                } else {
                    System.out.println("Aprovado!");
                    System.out.println("Média: " + segundaMedia);
                }
            }
        } else {
            System.out.println("Aprovado!");
            System.out.println("Média: " + primeiraMedia);
        }

    }
}
