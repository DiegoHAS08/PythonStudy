nomes = []
while True:
    nome = input("Digite um nome para cadastrar (ou 'sair'): ")
    if nome.lower() == "sair":
        break
    nomes.append(nome)
print("Nomes cadastrados:", nomes)
