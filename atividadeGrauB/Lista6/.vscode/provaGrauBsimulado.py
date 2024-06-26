# Função para validar se a resposta está entre 'a' e 'f'
def validar_resposta(resposta):
    return resposta in ['a', 'b', 'c', 'd', 'e', 'f']

# Cadastrar o gabarito
gabarito = []
print("Cadastre o gabarito da prova:")
for i in range(10):
    while True:
        resposta = input(f"Questão {i + 1}: ").lower()
        if validar_resposta(resposta):
            gabarito.append(resposta)
            break
        else:
            print("Resposta inválida! Por favor, entre com uma resposta entre 'a' e 'f'.")

# Entrar com as respostas do estudante
respostas_estudante = []
print("\nEntre com as respostas do estudante:")
for i in range(10):
    while True:
        resposta = input(f"Questão {i + 1}: ").lower()
        if validar_resposta(resposta):
            respostas_estudante.append(resposta)
            break
        else:
            print("Resposta inválida! Por favor, entre com uma resposta entre 'a' e 'f'.")

# Verificar quantas respostas estão corretas
corretas = 0
for i in range(10):
    if respostas_estudante[i] == gabarito[i]:
        corretas += 1

# Imprimir o resultado
print(f"\nNúmero de respostas corretas: {corretas} de 10")
