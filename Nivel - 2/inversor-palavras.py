while True:
    palavra = input("Digite uma palavra (ou 'sair'): ")
    if palavra.lower() == "sair":
        break
    print("Invertida:", palavra[::-1])
