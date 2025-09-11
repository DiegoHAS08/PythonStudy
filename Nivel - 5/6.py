try:
    with open("nomes.txt", "r") as arquivo:
        nomes = arquivo.read().splitlines()
        print("Nomes cadastrados:", nomes)
except FileNotFoundError:
    print("Arquivo 'nomes.txt' não encontrado.")
