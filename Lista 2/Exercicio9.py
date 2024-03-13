# 9. Durante uma liquidação uma loja resolveu dar quinze por cento de desconto nas compras feitas
# pelos clientes. Faça um programa que leia o valor da compra e escreva o valor da compra com o desconto.

precoVenda = float(input("Informe o valor da venda:"))
valorDesconto = (precoVenda * 15) / 100

valorLiquido = round(precoVenda - valorDesconto, 2)
print("A venda com 15 porcento de desconto ficou: R$",valorLiquido)