#7. Um criador de pássaros deseja saber a quantidade de ração diária necessária para alimentar seus
#pássaros. Cada pássaro consome 30 gramas de ração por dia. Escreva um programa que leia o
#número de pássaros que o criador possui e calcule a quantidade total de ração necessária por dia.

passaro = int(input("Informe quantos passaros o criador tem:"))
racao = 30

totalRacao = racao * passaro
print("O criador vai gastar",totalRacao,"gramas de ração por dia.")
