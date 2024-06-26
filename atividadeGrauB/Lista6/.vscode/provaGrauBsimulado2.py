import random

# Tamanho do tabuleiro
TAMANHO = 8

# Definição dos tipos de navios e seus tamanhos
navios = {
    'P': 5,  # Porta-aviões
    '4': 4,  # Navio de 4 canos
    '3': 3,  # Navio de 3 canos
    '2': 2,  # Navio de 2 canos
    'S': 1   # Submarino
}

# Função para inicializar as matrizes
def inicializar_matrizes():
    matriz_controle = [[' ' for _ in range(TAMANHO)] for _ in range(TAMANHO)]
    matriz_exibicao = [[' ' for _ in range(TAMANHO)] for _ in range(TAMANHO)]
    return matriz_controle, matriz_exibicao

# Função para posicionar os navios aleatoriamente
def posicionar_navios(matriz_controle):
    for tipo, tamanho in navios.items():
        orientacao = random.choice(['horizontal', 'vertical'])
        if orientacao == 'horizontal':
            while True:
                coluna = random.randint(0, TAMANHO - tamanho)
                linha = random.randint(0, TAMANHO - 1)
                if all(matriz_controle[linha][coluna + i] == ' ' for i in range(tamanho)):
                    for i in range(tamanho):
                        matriz_controle[linha][coluna + i] = tipo
                    break
        else:  # orientacao == 'vertical'
            while True:
                coluna = random.randint(0, TAMANHO - 1)
                linha = random.randint(0, TAMANHO - tamanho)
                if all(matriz_controle[linha + i][coluna] == ' ' for i in range(tamanho)):
                    for i in range(tamanho):
                        matriz_controle[linha + i][coluna] = tipo
                    break

# Função para verificar se o jogo terminou
def jogo_terminou(matriz_controle, matriz_exibicao):
    for linha in range(TAMANHO):
        for coluna in range(TAMANHO):
            if matriz_controle[linha][coluna] != ' ' and matriz_exibicao[linha][coluna] == ' ':
                return False
    return True

# Função principal do jogo
def jogo_batalha_naval():
    matriz_controle, matriz_exibicao = inicializar_matrizes()
    posicionar_navios(matriz_controle)
    jogadas = 0

    while not jogo_terminou(matriz_controle, matriz_exibicao):
        print('\nTabuleiro:')
        print('  1 2 3 4 5 6 7 8')
        print(' -----------------')
        for i in range(TAMANHO):
            print(chr(65 + i) + '|' + ' '.join(matriz_exibicao[i]) + '|')
        print(' -----------------')

        # Receber jogada do jogador
        jogada = input('Faça sua jogada (ex: A 5): ').strip().upper()
        linha = ord(jogada[0]) - 65
        coluna = int(jogada[2]) - 1

        if matriz_controle[linha][coluna] != ' ':
            tipo_navio = matriz_controle[linha][coluna]
            matriz_exibicao[linha][coluna] = tipo_navio
            print('BOOOM! Você acertou um navio!')
            if jogo_terminou(matriz_controle, matriz_exibicao):
                print('GLUB GLUB GLUB! Você afundou todos os navios!')
                print(f'Número de jogadas: {jogadas + 1}')
        else:
            matriz_exibicao[linha][coluna] = 'X'
            print('SPLASH! Água...')

        jogadas += 1

    print('Parabéns! Você venceu o jogo de Batalha Naval!')

# Executar o jogo
if __name__ == "__main__":
    jogo_batalha_naval()
