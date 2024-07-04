import csv

def carregar_dados(nome_arquivo):
    felinos = []
    try:
        with open(nome_arquivo, 'r') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                felinos.append(linha)
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando nova lista vazia.")
    return felinos

nome_arquivo = 'felinos.csv'
lista_felinos = carregar_dados(nome_arquivo)

def exibir_menu():
    print("\nMenu Principal:")
    print("1) Cadastrar felino")
    print("2) Alterar status de felino")
    print("3) Consultar informações sobre felino")
    print("4) Apresentar estatísticas gerais")
    print("5) Filtragem de dados")
    print("6) Salvar")
    print("7) Sair do programa")

exibir_menu()
opcao = int(input("Escolha uma opção: "))

def cadastrar_felino(lista_felinos):
    novo_felino = {}
    novo_felino['Nome'] = input("Nome do felino: ")
    novo_felino['Idade'] = input("Idade do felino: ")
    novo_felino['Sexo'] = input("Sexo (M/F): ")
    novo_felino['Raça'] = input("Raça do felino: ")
    novo_felino['Cor'] = input("Cor do felino: ")
    novo_felino['Castrado'] = input("Castrado (Sim/Não): ")
    novo_felino['Data de Resgate'] = input("Data de resgate (DD/MM/AAAA): ")
    novo_felino['Adotado'] = input("Adotado (Sim/Não): ")
    novo_felino['Contato'] = input("Número de celular do tutor: ")
    novo_felino['Tutor'] = input("Nome do tutor: ")
    novo_felino['FIV+'] = input("O gato possui FIV+ (Sim/Não): ")
    novo_felino['FELV+'] = input("O gato possui FELV+ (Sim/Não): ")
    novo_felino['Vacina'] = input("Data da última vacina: ")
    novo_felino['Extra'] = input("Informações extras: ")

    lista_felinos.append(novo_felino)
    print("\nFelino cadastrado com sucesso! Aqui estão os dados:")
    for chave, valor in novo_felino.items():
        print(f"{chave}: {valor}")


lista_felinos = []
cadastrar_felino(lista_felinos)


def alterar_status_felino(lista_felinos):
    if not lista_felinos:
        print("Não há felinos cadastrados.")
        return

    print("Lista de felinos:")
    for i, felino in enumerate(lista_felinos, start=1):
        print(f"{i}) {felino['Nome']} ({felino['Sexo']})")

    escolha = int(input("Escolha o número do felino que deseja alterar: ")) - 1
    felino_escolhido = lista_felinos[escolha]

    print(f"\nInformações do felino {felino_escolhido['Nome']}:\n")
    for chave, valor in felino_escolhido.items():
        print(f"{chave}: {valor}")

    while True:
        campo_alterar = input("Digite o nome do campo que deseja alterar (ou 'sair' para voltar ao menu principal): ")
        if campo_alterar.lower() == 'sair':
            break
        if campo_alterar in felino_escolhido:
            novo_valor = input(f"Digite o novo valor para {campo_alterar}: ")
            felino_escolhido[campo_alterar] = novo_valor
            print(f"{campo_alterar} atualizado para {novo_valor}.")
        else:
            print("Campo inválido. Tente novamente.")

    print("\nStatus do felino atualizado!")


def consultar_felino(lista_felinos):
    if not lista_felinos:
        print("Não há felinos cadastrados.")
        cadastrar_novo = input("Deseja cadastrar um novo felino? (Sim/Não): ")
        if cadastrar_novo.lower() == 'sim':
            cadastrar_felino(lista_felinos)
        else:
            print("Até mais!")
            return

    print("Lista de felinos:")
    for i, felino in enumerate(lista_felinos, start=1):
        print(f"{i}) {felino['Nome']} ({felino['Sexo']})")

    escolha = int(input("Escolha o número do felino que deseja consultar: ")) - 1
    felino_escolhido = lista_felinos[escolha]

    print(f"\nInformações do felino {felino_escolhido['Nome']}:\n")
    for chave, valor in felino_escolhido.items():
        print(f"{chave}: {valor}")

def calcular_estatisticas(lista_felinos):
    total_felinos = len(lista_felinos)
    machos = sum(felino['Sexo'] == 'M' for felino in lista_felinos)
    femeas = total_felinos - machos
    adotados = sum(felino['Adotado'] == 'Sim' for felino in lista_felinos)
    nao_adotados = total_felinos - adotados
    fiv_positivo = sum(felino['FIV+'] == 'Sim' for felino in lista_felinos)
    felv_positivo = sum(felino['FELV+'] == 'Sim' for felino in lista_felinos)

    print(f"Total de felinos: {total_felinos}")
    print(f"Machos: {machos} ({(machos / total_felinos) * 100:.2f}%)")
    print(f"Fêmeas: {femeas} ({(femeas / total_felinos) * 100:.2f}%)")
    print(f"Adotados: {adotados} ({(adotados / total_felinos) * 100:.2f}%)")
    print(f"Não adotados: {nao_adotados} ({(nao_adotados / total_felinos) * 100:.2f}%)")
    print(f"FIV+: {fiv_positivo} ({(fiv_positivo / total_felinos) * 100:.2f}%)")
    print(f"FELV+: {felv_positivo} ({(felv_positivo / total_felinos) * 100:.2f}%)")

calcular_estatisticas(lista_felinos)

def filtrar_felinos_por_periodo(lista_felinos):
    if lista_felinos:
        print("Não há felinos cadastrados.")
        return

    print("Escolha uma opção:")
    print("1) Consultar gatos resgatados por período")
    print("2) Para sair")

    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 1:
        ano_inicio = int(input("Digite o ano de início: "))
        ano_fim = int(input("Digite o ano de fim: "))
        felinos_resgatados = [felino for felino in lista_felinos if ano_inicio <= int(felino['Data de Resgate'][-4:]) <= ano_fim]
        print("\nFelinos resgatados no período:")
        for felino in felinos_resgatados:
            print(f"{felino['Nome']} ({felino['Sexo']})")
    elif opcao == 2:
        exibir_menu()
    else:
        print("Opção inválida. Tente novamente.")

filtrar_felinos_por_periodo(lista_felinos)


def salvar_dados(nome_arquivo, lista_felinos):
    try:
        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            campos = ['Nome', 'Idade', 'Sexo', 'Raça', 'Cor', 'Castrado', 'Data de Resgate',
                       'Adotado', 'Contato', 'Tutor', 'FIV+', 'FELV+', 'Vacina', 'Extra']
            escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
            escritor.writeheader()
            for felino in lista_felinos:
                escritor.writerow(felino)
        print("Dados salvos com sucesso no arquivo", nome_arquivo)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

nome_arquivo = 'felinos.csv'
lista_felinos = []  
salvar_dados(nome_arquivo, lista_felinos)

def main():
    nome_arquivo = 'felinos.csv'
    lista_felinos = carregar_dados(nome_arquivo)

    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_felino(lista_felinos)
        elif opcao == 2:
            alterar_status_felino(lista_felinos)
        elif opcao == 3:
            consultar_felino(lista_felinos)
        elif opcao == 4:
            calcular_estatisticas(lista_felinos)
        elif opcao == 5:
            filtrar_felinos_por_periodo(lista_felinos)
        elif opcao == 6:
            salvar_dados(nome_arquivo, lista_felinos)
        elif opcao == 7:
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()