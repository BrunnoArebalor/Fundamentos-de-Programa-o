# 4. Faça um algoritmo que permita ao aluno calcular a sua média final na Unisinos. 
# Leia a nota do grau A e do grau B e escreva o resultado na tela. 
# Lembrando que o Grau A vale 1/3 e o Grau B 2/3.

grauA = float(input("Informe a nota do Grau A:"))
grauB = float(input("Informe a nota do Grau B:"))

notaFinal = (grauA + (grauB * 2)) / 3
print(notaFinal)