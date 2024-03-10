# 3. Um restaurante de buffet a quilo cobra R$ 40,00 por quilo.
# Escreva um programa que leia o peso do prato do cliente e calcule o valor a ser pago.

grauA = int(input("Informe a nota do Grau A:"))
grauB = int(input("Informe a nota do Grau B:"))

notaFinal = (grauA + (grauB * 2)) / 3
print(notaFinal)