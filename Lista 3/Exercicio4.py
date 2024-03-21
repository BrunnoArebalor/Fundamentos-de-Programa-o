# 4) Crie um programa que verifica se um número inteiro informado pelo usuário é divisível por 3.

numero = int(input("Informe um número para ver se ele é divisivel por 3:"))

if numero % 3 == 0 :
    print("Número divisível por 3!")
else :
    print("Não é divisível!")