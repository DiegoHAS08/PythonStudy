contatos = {}
while True:
    nome = input("Digite o nome do contato (ou 'sair'): ")
    if nome.lower() == "sair":
        break
    telefone = input(f"Digite o telefone de {nome}: ")
    contatos[nome] = telefone
print("Lista de contatos:", contatos)
