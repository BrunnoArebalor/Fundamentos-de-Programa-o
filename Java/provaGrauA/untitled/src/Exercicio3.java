import java.util.Scanner;
public class Exercicio3 {
    public static void main(String[] args) {
        System.out.println("QUESTÃO 3");

        Scanner sc = new Scanner(System.in);
        System.out.println("Digite a operação que queres fazer:");

        System.out.println("Verificar quantidade de poções em estoque tecle 1");
        System.out.println("Fabricar uma poção tecle 2");
        System.out.println("Sair tecle 3");

        int poDeFenix = 100;
        int essenciaCelestial = 50;
        int raizDeDragao = 45;
        int orvalhoLunar = 30;
        int floresSecas = 200;
        int elixirAmargo = 20;
        int lagrimasDeUnicornio = 15;

        int opcao = sc.nextInt();

        if (opcao == 1) {
            System.out.println("      INGREDIENTES    | QUANTIDADE INICAIL");
            System.out.println("          Pó de Fenix | " + poDeFenix);
            System.out.println("   Essência Celestial | " + essenciaCelestial);
            System.out.println("       Raiz de Dragão | " + raizDeDragao);
            System.out.println("        Orvalho Lunar | " + orvalhoLunar);
            System.out.println("         Flores Secas | " + floresSecas);
            System.out.println("        Elixir Amargo | " + elixirAmargo);
            System.out.println("Lagrimas de Unicornio | " + lagrimasDeUnicornio);

            System.out.println("Deseja preparar uma opção tecle 2");
            System.out.println("Deseja sair tecle 3");
            opcao = sc.nextInt();

            if (opcao == 2) {
                System.out.println("Qual poção deseja:");
                System.out.println("Poção 1: poção de cura");
                System.out.println("Poção 2: poção da força da floresta");
                System.out.println("Poção 3: poção sabedoria da riqueza");
                System.out.println("Poção 4: poção da sorte no amor");
                System.out.println("Poção 5: poção malvada");

                System.out.println("Quantas poções vc quer:");
                int qtdPocao = sc.nextInt();
                System.out.println("Qual poção:");
                int pocao = sc.nextInt();

                for (int i = 0; i < qtdPocao; i++ ) {
                    if (pocao == 1) {
                        if (poDeFenix > 30 && essenciaCelestial > 20 && floresSecas > 20 && lagrimasDeUnicornio > 10) {
                            System.out.println("Poção Criada com sucesso!");
                            poDeFenix -= 30;
                            essenciaCelestial -= 30;
                            floresSecas -= 20;
                            lagrimasDeUnicornio -= 10;
                        } else {
                            System.out.println("Faltou ingredietes para a criação da poção!");
                        }
                    } else if (pocao == 2) {
                        if (orvalhoLunar > 20 && raizDeDragao > 30 && floresSecas > 30) {
                            System.out.println("Poção Criada com sucesso!");
                            orvalhoLunar -= 30;
                            raizDeDragao -= 30;
                            floresSecas -= 30;
                        } else {
                            System.out.println("Faltou ingredietes para a criação da poção!");
                        }
                    } else if (pocao == 3) {
                        if (essenciaCelestial > 30 && poDeFenix > 50) {
                            System.out.println("Poção Criada com sucesso!");
                            essenciaCelestial -= 30;
                            poDeFenix -= 50;
                        } else {
                            System.out.println("Faltou ingredietes para a criação da poção!");
                        }
                    } else if (pocao == 4) {
                        if (orvalhoLunar > 10 && floresSecas > 50 && lagrimasDeUnicornio > 5) {
                            System.out.println("Poção Criada com sucesso!");
                            orvalhoLunar -= 10;
                            floresSecas -= 50;
                            lagrimasDeUnicornio -= 5;
                        }
                    } else if (pocao == 5) {
                        if (elixirAmargo > 10 && raizDeDragao > 15) {
                            System.out.println("Poção Criada com sucesso!");
                            elixirAmargo -= 10;
                            raizDeDragao -= 15;
                        }
                    }
                }

            }
        } else if (opcao == 2) {
            if (opcao == 2) {
                System.out.println("Qual poção deseja:");
                System.out.println("Poção 1: poção de cura");
                System.out.println("Poção 2: poção da força da floresta");
                System.out.println("Poção 3: poção sabedoria da riqueza");
                System.out.println("Poção 4: poção da sorte no amor");
                System.out.println("Poção 5: poção malvada");

                System.out.println("Quantas poções vc quer:");
                int qtdPocao = sc.nextInt();
                System.out.println("Qual poção:");
                int pocao = sc.nextInt();

                for (int i = 0; i < qtdPocao; i++ ) {
                    if (pocao == 1) {
                        if (poDeFenix > 30 && essenciaCelestial > 20 && floresSecas > 20 && lagrimasDeUnicornio > 10) {
                            System.out.println("Poção Criada com sucesso!");
                            poDeFenix -= 30;
                            essenciaCelestial -= 30;
                            floresSecas -= 20;
                            lagrimasDeUnicornio -= 10;
                        } else {
                            System.out.println("Faltou ingredietes para a criação da poção!");
                        }
                    } else if (pocao == 2) {
                        if (orvalhoLunar > 20 && raizDeDragao > 30 && floresSecas > 30) {
                            System.out.println("Poção Criada com sucesso!");
                            orvalhoLunar -= 30;
                            raizDeDragao -= 30;
                            floresSecas -= 30;
                        } else {
                            System.out.println("Faltou ingredietes para a criação da poção!");
                        }
                    } else if (pocao == 3) {
                        if (essenciaCelestial > 30 && poDeFenix > 50) {
                            System.out.println("Poção Criada com sucesso!");
                            essenciaCelestial -= 30;
                            poDeFenix -= 50;
                        } else {
                            System.out.println("Faltou ingredietes para a criação da poção!");
                        }
                    } else if (pocao == 4) {
                        if (orvalhoLunar > 10 && floresSecas > 50 && lagrimasDeUnicornio > 5) {
                            System.out.println("Poção Criada com sucesso!");
                            orvalhoLunar -= 10;
                            floresSecas -= 50;
                            lagrimasDeUnicornio -= 5;
                        }
                    } else if (pocao == 5) {
                        if (elixirAmargo > 10 && raizDeDragao > 15) {
                            System.out.println("Poção Criada com sucesso!");
                            elixirAmargo -= 10;
                            raizDeDragao -= 15;
                        }
                    }
                }

            }
        } else {
            System.out.println("Saindo do programa...");
        }
    }
}
