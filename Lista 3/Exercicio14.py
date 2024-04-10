# 14) Criar um programa para identificar o valor a ser pago por um plano de saúde dada a idade do
# conveniado considerando que todos pagam R$ 300 e mais um adicional (se tiver dependentes)
# conforme a seguinte tabela:
# a) crianças com menos de 10 anos pagam R$100;
# b) dependentes com idade entre 10 e 30 anos pagam R$220;
# c) dependentes com idade entre 31 e 60 anos pagam R$ 395; e

idadeConveniado = int(input("Quantos anos o conveniado tem:"))
resposta = str(input("S/N"))

while resposta == 'S' or resposta == 'N':
    if resposta == 'S' :
        qtdDependente = int(input("Quantos depentes o conveniado tem:"))
        if qtdDependente == 1 :
            idadeDependente = int(input("qual idade do dependente:"))
            valorPlano = idadeDependente + 300
        elif qtdDependente == 2 :
            idadeDependente = int(input("qual idade do primeiro dependente:"))
            idadeDependente2 = int(input("qual idade do segundo dependente:"))
            valorPlano 

