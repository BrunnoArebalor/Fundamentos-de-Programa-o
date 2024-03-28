# 7) Implementar um programa que calcula o desconto previdenciário de um funcionário. O programa
# deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto
# segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é
# 318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20.

salario = float(input("Informe o seu salário:"))
descSalario = (salario * 11) / 100

if descSalario <= 318.20 :
    salarioFinal = salario - descSalario
    print("O seu salário com os descontos ficou: R$", salarioFinal)
    print("Os descontos ficaram: R$", descSalario)
else :
    salarioFinal = salario - 318.20
    print("O seu salário com os descontos ficou: R$", salarioFinal)