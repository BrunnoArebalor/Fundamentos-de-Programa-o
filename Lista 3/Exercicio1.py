# 1) Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for
# diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.

print("Informe dois numeros para serem divididos e ver se é diferente de ZERO")
numero1 = float(input("Primeiro número:"))
numero2 = float(input("Segundo número:"))

resultado = numero1 / numero2
if resultado == 0 :
    print("Valor igual a ZERO!")
else :
    print("Valor diferente de Zero!")