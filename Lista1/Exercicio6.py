# 6. A loja de eletrônicos TechMundo vende uma certa quantidade de smartphones e uma quantidade
# de tablets a cada dia. Cada smartphone custa R$ 1000,00 e cada tablet custa R$ 1500,00. 
# Ao final do dia, o dono quer saber quanto arrecadou com a venda dos smartphones e dos tablets.
# Escreva um programa que leia o número de smartphones e tablets vendidos em um dia e calcule o total arrecadado

smartphone = int(input("Informe a quantidade vendida de Smartphone:"))
tablet = int(input("Informe a quantidade vendida de Tablet:"))

smartphonePreco = 1000
tabletPreco = 1500

smartphoneTotal = smartphone * smartphonePreco
tabletTotal = tablet * tabletPreco

