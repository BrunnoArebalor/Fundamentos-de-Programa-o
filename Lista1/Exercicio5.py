# 5. Um motorista deseja encher o tanque do seu carro com gasolina.
# Escreva um algoritmo para ler o preço do litro da gasolina e o valor que o motorista tem disponível para abastecer.
# Calcule quantos litros ele conseguiu colocar no tanque e exiba na tela

valorDisponivel = float(input("Informe o valor que o cliente vai por de gasolina:"))
gasolina = 5.59

litro = round(valorDisponivel / gasolina, 2)

print("Cliente abasteceu",litro,"litros")