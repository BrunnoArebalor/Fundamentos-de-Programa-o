import java.util.Scanner;
public class Exercicio12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Qual a idade do atleta:");
        int idade = sc.nextInt();

        if (idade >= 5 && idade <= 8) {
            System.out.println("Para essa idade o atleta vai competir na Infantil A!");
            System.out.println("Idade: " + idade);
        } else if (idade >= 8 && idade <= 10) {
            System.out.println("Para essa idade o atleta vai competir na Infantil B!");
            System.out.println("Idade: " + idade);
        } else if (idade >= 11 && idade <= 14) {
            System.out.println("Para essa idade o atleta vai competir na Juvenil A!");
            System.out.println("Idade: " + idade);
        } else if (idade >= 18 && idade <= 17) {
            System.out.println("Para essa idade o atleta vai competir na Infantil B!");
            System.out.println("Idade: " + idade);
        } else if (idade < 5) {
            System.out.println("Idade não se encaixa para competir!");
            System.out.println("Idade: " + idade);
        }
        else {
            System.out.println("Para essa idade o atleta vai competir na Sênior!");
            System.out.println("Idade: " + idade);
        }
    }
}
