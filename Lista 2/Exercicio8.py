# 8. Um usuário deseja converter a temperatura de Celsius para Fahrenheit. Escreva um programa que
# leia a temperatura em Celsius e exiba a temperatura equivalente em Fahrenheit.

celsius = float(input("Informe um valor em celsius para converter em fahrenheit:"))
fahrenheit = (celsius * 1.8) + 32

print("O valor da conversão é:",fahrenheit,"°F")