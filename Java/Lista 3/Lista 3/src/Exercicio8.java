import java.util.Scanner;
public class Exercicio8 {
    public static void main(String[] args) {
        /*
        8) Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor
        da compra. Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço
        for de até 50 reais e lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na
        tela o valor de venda
        */
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite o valor da venda:");
        double venda = sc.nextDouble();

        if (venda < 20) {
            double vendaLucro = (venda * 45) / 100;
            double vendaValor = venda + vendaLucro;
            System.out.printf("Valor da venda: R$%.2f\n", vendaValor);
            System.out.printf("Valor do lucro da venda: R$%.2f", vendaLucro);
        } else if (venda < 50) {
            double vendaLucro = (venda * 35) / 100;
            double vendaValor = venda + vendaLucro;
            System.out.printf("Valor da venda: R$%.2f\n", vendaValor);
            System.out.printf("Valor do lucro da venda: R$%.2f", vendaLucro);
        } else {
            double vendaLucro = (venda * 25) / 100;
            double vendaValor = venda + vendaLucro;
            System.out.printf("Valor da venda: R$%.2f\n", vendaValor);
            System.out.printf("Valor do lucro da venda: R$%.2f", vendaLucro);
        }
    }
}
