import java.util.Scanner;
import java.util.Random;
public class Exercicio6 {
    public static void main(String[] args) {
        /*
        6) Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois
        disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie
        um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da
        soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga
        que o programa venceu.
        */
        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Jogo de Par ou Ímpar");
        System.out.println("Digite 1 para ÍMPAR e 2 para PAR:");
        int jogada1 = sc.nextInt();

        System.out.println("Digite um número de 0 a 5");
        int jogada2 = sc.nextInt();
        int bot = random.nextInt(0, 5);

        int resultado = jogada2 + bot;

        if (resultado % 2 == 0 && jogada1 == 1) {
            System.out.println("Deu PAR!!!");
            System.out.println("Você jogou ÍMPAR e perdeu!!!");
            System.out.println("Número que vc jogou: " + jogada2);
            System.out.println("Número que o adversário jogou: " + bot);
        } else if (resultado % 2 == 0 && jogada1 == 2) {
            System.out.println("Deu PAR!!!");
            System.out.println("Você jogou PAR e venceu!!!");
            System.out.println("Número que vc jogou: " + jogada2);
            System.out.println("Número que o adversário jogou: " + bot);
        } else if (resultado % 2 == 1 && jogada1 == 1) {
            System.out.println("Deu ÍMPAR!!!");
            System.out.println("Você jogou ÍMPAR e venceu!!!");
            System.out.println("Número que vc jogou: " + jogada2);
            System.out.println("Número que o adversário jogou: " + bot);
        } else {
            System.out.println("Deu PAR!!!");
            System.out.println("Você jogou PAR e perdeu!!!");
            System.out.println("Número que vc jogou: " + jogada2);
            System.out.println("Número que o adversário jogou: " + bot);
        }

    }
}
