nomes = []
while True:
    nome = input("Digite um nome (ou 'sair'): ")
    if nome.lower() == "sair":
        break
    nomes.append(nome)

with open("nomes.txt", "w") as arquivo:
    for n in nomes:
        arquivo.write(n + "\n")

print("Nomes salvos em 'nomes.txt'.")
