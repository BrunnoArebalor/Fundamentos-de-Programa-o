# 2) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor 
# que A + C.

A = int(input("Informe o valor de A:"))
B = int(input("Informe o valor de B:"))
C = int(input("Informe o valor de C:"))

somaAb = A + B
somaAc = A + C

if somaAb > somaAc :
    print("Soma de A+B maior que soma de A+C!")
elif somaAb < somaAc :
    print("Soma de A+C maior que soma de A+B")

