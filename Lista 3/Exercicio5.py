# 5) Faça um algoritmo para receber um número qualquer do usuário e informar na tela se é par ou se
# é ímpar.

numero = int(input("Informe um número para descobrir de é impar ou par:"))

if numero % 2 == 0 :
    print("Número é PAR!")
else :
    print("Número é IMPAR!")