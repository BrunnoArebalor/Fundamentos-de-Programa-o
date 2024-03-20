# 10. O lojista gostou tanto do seu programa anterior que encomendou outro. Dessa vez ele quer que
# você calcule quanto cada cliente gastou na loja apenas informando o número de camisetas, calças
# e cintos comprados. As camisetas custam R$ 25,00, as calças cem reais e os cintos 40 reais. Some o
# valor da compra e ao final dê um desconto de 10 por cento sobre o total. Exiba na tela o valor do
# desconto e o valor da compra.

print("CAIXA")
qtdCamisa = int(input("Informe quantas camisas o cliente levou:"))
qtdCalca = int(input("Informe quantas calças o cliente levou:"))
qtdCinto = int(input("Informe quantas cintos o cliente levou:"))

valorCamisa = 25.00
valorCalca = 100.00
valorCinto = 40.00

totalCamisa = qtdCamisa * valorCamisa
totalCalca = qtdCalca * valorCalca
totalCinto = qtdCinto * valorCinto

valorTotal = totalCamisa + totalCalca + totalCinto
valorDesconto = (valorTotal * 10) / 100
valorLiquido = valorTotal - valorDesconto
print("A compra do clinte ficou no valor de: R$",valorLiquido)


