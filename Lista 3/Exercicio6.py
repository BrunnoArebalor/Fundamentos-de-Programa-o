# 6) Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois
# disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie
# um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da
# soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga
# que o programa venceu.

import random

print("JOGO DE PAR OU IMPAR")
jogada1 = int(input("Escolha 1 para IMPAR e 2 para PAR:"))
jogada2 = int(input("escolha um número de 0 a 5 para jogar:"))
adiversario = random.randint(0, 5)
resultado = jogada2 + adiversario

if resultado % 2 == 0 :
    print("DEU PAR!")
    print("adiversário jogou:", adiversario)
else :
    print("DEU IMPAR")
    print("adiversário jogou:", adiversario)