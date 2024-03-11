contatos = []

def adicionar_contato():
    nome = input("Digite o nome de contato: ")
    telefone = int(input("Digite o número de telefone: "))
    contatos.append((nome,telefone))
    print(contatos)
    print("Contado adicionado com sucesso!")

def buscar_contato():
    nome = input("Digite o nome de contato que deseja buscar: ")
    if nome in contatos:
        print(f"Nome de Contado: {nome} - Número de telefone: ")
    else:
        print("Contado não encontrado")

adicionar_contato()
buscar_contato()