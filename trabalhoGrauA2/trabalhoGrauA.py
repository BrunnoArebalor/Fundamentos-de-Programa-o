import random

def girarRoleta():
    return random.randint(1, 6)

def moverJogador(jogador, casas):
    if jogador['posicao'] == 2:
        print("Que azar! Você caiu em uma armadilha e morreu!")
        return True  # Retorna True para indicar que o jogador morreu
    else:
        jogador['posicao'] += casas
        return False

def executarAcaoJogador(jogador):
    print("Você está na casa!", jogador['posicao'])

def posicaoJogadores():
    jogador1 = {'posicao': 0}
    jogador2 = {'posicao': 0}

    while True:
        print("Bem-vindos ao Jogo da Vida!")
        input("Pressione ENTER para girar a roleta...")
        resultado = girarRoleta()
        print("Jogador 1 girou a roleta e obteve:", resultado)

        # ===== REGRAS DO JOGO ===== #

        if moverJogador(jogador1, resultado):
            print("Jogador 1 morreu! Fim de jogo para ele.")
            break

        # ===== CONDIÇÕES DO JOGO ===== #

        # verifica numero 3 da roleta #
        if resultado == 3:
            print("Que azar! Você tirou 3 e vai voltar uma casa.")
            moverJogador(jogador1, -1)
        else: 
            moverJogador(jogador1, resultado)
        # verifica numero 6 da roleta #
        if resultado == 6:
            print("Que azar! Você tirou 6! Não ande nenhuma casa.")
        else:
            # verifica venceu #
            if jogador1['posicao'] >= 21:
                print("Parabéns, Jogador 1! Você venceu!")
                break

        
        
        executarAcaoJogador(jogador1, jogador1['posicao'])

        # ===== VERIFICA JOGADOR 2 ===== #
        if input("Pressione Enter para o próximo jogador ou 'q' para sair: ") == 'q':
            break

        print("Bem-vindos ao Jogo da Vida!")
        input("Pressione ENTER para girar a roleta...")
        resultado = girarRoleta()
        print("Jogador 2 girou a roleta e obteve:", resultado)

        # ===== REGRAS DO JOGO ===== #

        if moverJogador(jogador2, resultado):
            print("Jogador 2 morreu! Fim de jogo para ele.")
            break

        # ===== CONDIÇÕES DO JOGO ===== #
    
        # verifica numero 3 da roleta #
        if resultado == 3:
            print("Que azar! Você tirou 3 e vai voltar uma casa.")
            moverJogador(jogador2, -1)
        else: 
            moverJogador(jogador2, resultado)
        # verifica numero 6 da roleta #
        if resultado == 6:
            print("Que azar! Você tirou 6! Não ande nenhuma casa.")
        else: 
            # verifica venceu #
            if jogador2['posicao'] >= 21:
                print("Parabéns, Jogador 2! Você venceu!")
                break

        
        executarAcaoJogador(jogador2, jogador2['posicao'])

        

posicaoJogadores()



    
    
    