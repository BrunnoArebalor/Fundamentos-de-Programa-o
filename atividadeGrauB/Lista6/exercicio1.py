# 1. Criar um vetor de 10 números v e inicialize-o sorteando valores de 10 a 90 para cada elemento.
#Depois disso, implemente algoritmos para:
#a. Imprimir o vetor
#b. Verificar se existe o valor 50 neste vetor (apenas dizer se encontrou ou não)
#c. Verificar o número de ocorrências do valor 50 neste vetor.
#d. Calcular a média dos valores do vetor
#e. Encontrar o maior e o menor valor dos elementos do vetor.
#f. Imprimir a soma e o produto acumulado dos valores dos elementos do vetor
#g. Imprimir o vetor em ordem inversa
#h. Copiar os elementos em ordem inversa para outro vetor.
#i. Crie outros dois vetores com 10 elementos, vPares e vImpares. Copie para vPares todos os
#elementos pares e para vImpares todos os elementos ímpares. Depois disso, imprima o
#conteúdo de vPares e vImpares.

import random
import statistics

# Definir o tamanho do vetor
tamanho_vetor = 10

# Inicializar o vetor com valores sorteados entre 10 e 90
vetor = [random.randint(10, 90) for _ in range(tamanho_vetor)]

# Verificar se o valor 50 está presente no vetor
valor_procurado = 50
encontrado = valor_procurado in vetor

# Contar o número de ocorrências do valor 50 no vetor
ocorrencias = vetor.count(valor_procurado)

# Calcular a média dos valores do vetor usando o módulo statistics
media = statistics.mean(vetor)

# Encontrar o maior e o menor valor dos elementos do vetor
maior_valor = max(vetor)
menor_valor = min(vetor)

# Imprimir o vetor e o resultado da verificação
print("Vetor:", vetor)
if encontrado:
    print(f"O valor {valor_procurado} foi encontrado no vetor.")
else:
    print(f"O valor {valor_procurado} não foi encontrado no vetor.")

print(f"O valor {valor_procurado} apareceu {ocorrencias} vez(es) no vetor.")

print(f"A média dos valores do vetor é {media:.2f}.")

print(f"O maior valor do vetor é {maior_valor}.")
print(f"O menor valor do vetor é {menor_valor}.")