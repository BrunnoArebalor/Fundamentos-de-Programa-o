# 3. Um restaurante de buffet a quilo cobra R$ 40,00 por quilo.
# Escreva um programa que leia o peso do prato do cliente e calcule o valor a ser pago.

peso = int(input("Informe o peso em gramas do prato da cliente:"))

preco = round(peso * 0.04, 2)

print("O valor do prato da cliente ficou R$",preco)