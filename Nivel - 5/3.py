with open("saida.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(f"O arquivo tem {len(linhas)} linhas.")
